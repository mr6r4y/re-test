-- IP address of our sniffing machine, change this to your IP address
hostip = "192.168.1.25"

-- define the function which determines incoming or outgoing
local function getdestination(src,dst)
    if tostring(src) == hostip then
        return "outgoing"
    end
    if tostring(dst) == hostip then
        return "incoming"
    end
end

local function register_ipdirection_postdissector()
    -- create the protocol dissector called direction
    local proto = Proto('direction', 'direction dissector')
    -- create a protofield
    local direction = ProtoField.string('direction.direction', 'direction', 'direction')
    -- assign the protofield to our protocol dissector
    proto.fields = {direction}
    -- create variables for the packet fields we are interested in getting access to
    local source = Field.new('ip.src')
    local dest = Field.new('ip.dst')
    -- define the post-dissector, this is what we use to add new columns

    function proto.dissector(buffer, pinfo, tree)
        local ipsrc = source()
        local ipdst = dest()
        -- if we have an ip source then add our tree calling our direction function
        if ipsrc ~= nil then
            -- create our TreeItem
            local stree = tree:add(proto, 'Direction')
            stree:add(direction, getdestination(ipsrc.value,ipdst.value))
        end
    end

    -- register the post-dissector
    register_postdissector(proto)
end

local function Main()
    register_ipdirection_postdissector()
end

Main()
