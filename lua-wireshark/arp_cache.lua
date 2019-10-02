do
    --filter on either arp or IP packets (so all packets with a MAC to IP mapping)
    local new_filter = "arp || ip"
    -- we want the src of the arp packet (remember arp doesn't have an IP header)
    local arp_ip = Field.new("arp.src.proto_ipv4")
    local eth_src = Field.new("eth.src")
    local ip_src = Field.new("ip.src")
    -- create an empty table that will become our ip to mac address mapping
    local arp_cache = {}

    -- create our function to run that creates the listener
    local function init_listener()
        -- create our listner, filtering on either ARP or IP packets
        local tap = Listener.new(nil, new_filter)

        --called for every packet
        function tap.packet(pinfo, tvb)
                -- create the local variables holding our fields
            local arp_ip = arp_ip()
            local eth_src = eth_src()
            local ip_src = ip_src()

            -- explicity checking to see arpip does not equal nil
            if tostring(arp_ip) ~= "nil" then
                -- if it isn't nil then we pull the ARP source IP and map it to the MAC address in the Ethernet Source field
                if not arp_cache[tostring(arp_ip)] then
                    print("[*] (" .. tostring(arp_ip) .. ") at " .. tostring(eth_src))
                end
                arp_cache[tostring(arp_ip)] = tostring(eth_src)
            else
                if not arp_cache[tostring(ip_src)] then
                    print("[*] (" .. tostring(ip_src) .. ") at " .. tostring(eth_src))
                end
                -- if the ARP source IP field is nil then we get
                -- access to the packet source via pinfo which is how we access columns
                -- and map it to the Ethernet Source field (MAC address)
                arp_cache[tostring(ip_src)] = tostring(eth_src)
                --end of main if block
            end
            --end of tap.packet()
        end

        -- just defining an empty tap.reset function
        function tap.reset()
            --end of tap.reset()
        end

        -- define the draw function to print out our created arp cache.
        function tap.draw()
            -- iterate over the keys/values within our arp_cache table and print out the IP to MAC mapping
            -- for ip,mac in pairs(arp_cache) do
            --     print("[*] (" .. ip .. ") at " .. mac)
            --end of for block
            -- end
        --end of tap.draw()
        end
    --end of init_listener()
    end
    -- call the init_listener function
    init_listener()
--end of everything
end
