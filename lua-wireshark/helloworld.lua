local function HelloWorldListener()
    -- creating the listener with a filter for 'http'
    local listener = Listener.new(nil, 'http')

    function listener.packet(pinfo, tvb)
        -- this is called for every packet meeting the filter,
        -- i.e. 'http' in this example
    end

    function listener.draw()
        print('Hello World')
    end
end

HelloWorldListener()