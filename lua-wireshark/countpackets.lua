-- variables for our counters
local httpcounter = 0
local smbcounter = 0
local icmpcounter = 0
local vrrpcounter = 0

-- function to create our listner
local function HelloWorldListener()
    -- create our listener with no filter
    local listener = Listener.new(nil, '')

    -- create the variables which will hold our fields for each packet
    local proto = Field.new('ip.proto')
    local httpfield = Field.new('http')
    local smbfield = Field.new('smb')
    local icmpfield = Field.new('icmp')
    local vrrpfield = Field.new('vrrp')

    -- define the listener.packet function which is called for every packet

    function listener.packet(pinfo, tvb)
        -- local variable for out ip.proto field
        local protocolnumber = proto()

        -- check to see if the packet has an ICMP field, if so increment the ICMP counter
        if(icmpfield()) then
            icmpcounter = icmpcounter+1
        end

        -- check to see if the packet has a VRRP field, if so increment the VRRP counter
        if(vrrpfield()) then
            vrrpcounter = vrrpcounter+1
        end

        -- see if the IP protocol is 6, aka TCP, if so then check for both HTTP and SMB
        if(protocolnumber and protocolnumber.value == 6) then
            local http = httpfield()
            local smb = smbfield()

            if http then
                httpcounter = httpcounter+1
            end
            if smb then
                smbcounter = smbcounter+1
            end
        end
    end

    -- create the draw function which will display our counters
    function listener.draw()
        print(string.format("HTTP: %i", httpcounter))
        print(string.format("SMB: %i", smbcounter))
        print(string.format("VRRP: %i", vrrpcounter))
        print(string.format("ICMP: %i", icmpcounter))
    end
end

-- run our listener function
HelloWorldListener()