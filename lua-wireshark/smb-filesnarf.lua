local function printfiles(table)
    for key, value in pairs(table) do
        print(key .. ': ' .. value)
    end
end

function string.unhexlify(str)
    return (str:gsub('..', function (byte)
        if byte == "00" then
            return "\0"
        end
        return string.char(tonumber(byte, 16))
    end))
end

local function SMBFileListener()
    local oFilter = Listener.new(nil, 'smb')
    local oField_smb_file = Field.new('smb.file')
    local oField_smb_file_data = Field.new('smb.file_data')
    local oField_smb_eof = Field.new('smb.end_of_file')
    local oField_smb_cmd = Field.new('smb.cmd')
    local oField_smb_len_low = Field.new('smb.data_len_low')
    local oField_smb_offset = Field.new('smb.file.rw.offset')
    local oField_smb_response = Field.new('smb.flags.response')
    local gFiles = {}

    function oFilter.packet(pinfo, tvb)
        if(oField_smb_cmd()) then
            local cmd = oField_smb_cmd()
            local smb_response = oField_smb_response()
            if(cmd.value == 0xa2 and smb_response.value == true) then
                local sFilename = tostring(oField_smb_file())
                sFilename = string.gsub(sFilename,"\\", "_")
                local iFilesize = oField_smb_eof()
                iFilesize = tonumber(tostring(iFilesize))
                if(iFilesize > 0) then
                    gFiles[sFilename] = iFilesize
                end
            end
            if(cmd.value == 0x2e and smb_response.value == true) then
                local sFilename = tostring(oField_smb_file())
                sFilename = string.gsub(sFilename,"\\", "_")
                local iOffset = tonumber(tostring(oField_smb_offset()))
                local file_len_low = tonumber(tostring(oField_smb_len_low()))
                local file = io.open(sFilename,'r+')
                if(file == nil) then
                    file = io.open(sFilename,'w')
                    local tempfile = string.rep("A", gFiles[sFilename])
                    file:write(tempfile)
                    file:close()
                    file = io.open(sFilename, 'r+')
                end
                if(file_len_low > 0) then
                    local file_data = tostring(oField_smb_file_data())
                    file_data = string.gsub(file_data,":", "")
                    file_data = file_data:unhexlify()
                    file:seek("set",iOffset)
                    file:write(file_data)
                    file:close()
                end
            end
        end
    end

    function oFilter.draw()
        printfiles(gFiles) -- list filename and sizes
    end
end

SMBFileListener()
