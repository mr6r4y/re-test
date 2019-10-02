-- url decode function
function url_decode(str)
    str = string.gsub (str, "+", " ")
    str = string.gsub (str, "%%(%x%x)", function(h) return string.char(tonumber(h,16)) end)
    str = string.gsub (str, "\r\n", "\n")
    return str
end

local function check(packet)
    --[[ this is a trivial (to bypass) example check for
    a query string that contains an html script
    element with an alert keyword, indicitive of xss
    --]]
    local result = url_decode(tostring(packet))
    result = string.match(result, "<script>alert.*")
    if result ~= nil then
        return true
    else
        return false
    end
end

local function register_suspicious_postdissector()
    local proto = Proto('suspicious', 'suspicious dissector')
    --create a new expert field for the proto
    exp_susp = ProtoExpert.new('suspicious.expert', 'Potential Refelctive XSS', expert.group.SECURITY, expert.severity.WARN)
    --register the expert field
    proto.experts = {exp_susp}

    function proto.dissector(buffer, pinfo, tree)
        --[[ this just searches through all of the packet
        buffer, this could also be implemented by
        pulling the http.request.uri field and search
        on that --]]
        local range = buffer:range()
        if check(range:string()) then
        --[[ if the check returns true then add
        a suspicious field to the packet tree
        and add the expert info --]]
            local stree = tree:add(proto, 'Suspicious')
            stree:add_proto_expert_info(exp_susp)
        end
    end

    register_postdissector(proto)
end

register_suspicious_postdissector()
