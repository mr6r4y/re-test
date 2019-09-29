do
    packets = 0;
    local function init_listener()
        local tap = Listener.new()
        function tap.reset()
            packets = 0;
        end
        function tap.packet(pinfo,tvb,ip)
            packets = packets + 1
        end
        function tap.draw()
            print("Packets ",packets)
        end
    end
    init_listener()
end