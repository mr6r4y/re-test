--create the protocol
sample_proto = Proto("sample", "w4sp sample protocol")

--create the fields so we can match on them in the filter box
local f_len_h = ProtoField.uint16("sample.len_h", "Length", base.HEX, nil, nil, "This is the Length")
local f_len_d = ProtoField.uint16("sample.len_d", "Length", base.DEC, nil, nil, "This is the Length")

--transid is only a single byte so uint8
local f_transid_d = ProtoField.uint8("sample.transid_d", "Trans ID", base.DEC, nil, nil, "This is the Transaction ID")
local f_transid_h = ProtoField.uint8("sample.transid_h", "Trans ID", base.HEX, nil, nil, "This is the Transaction ID")

--show both string and int
local f_msgtype_s = ProtoField.string("sample.msgtype_s", "MsgType", "This is the Message Type")
local f_msgtype_uh = ProtoField.uint8("sample.msgtype_uh", "MsgType", base.HEX, nil, nil, "This is the Message Type")
local f_msgtype_ud = ProtoField.uint8("sample.msgtype_ud", "MsgType", base.DEC, nil, nil, "This is the Message Type")

--create the data fields
local f_msgdata = ProtoField.string("sample.msgdata", "MsgData", "This is Message Data")
local f_addata = ProtoField.string("sample.addata", "AddData", "This is Additional Data")
local f_addata_b = ProtoField.bytes("sample.addata_b", "AddData_bytes", base.HEX, nil, nil, "This is Additional data as bytes")

--add fields to our protocol
sample_proto.fields = {
    f_len_h,
    f_len_d,
    f_transid_h,
    f_transid_d,
    f_msgtype_s,
    f_msgtype_uh,
    f_msgtype_ud,
    f_msgdata,
    f_addata,
    f_addata_b,
}

--create our dissector
function sample_proto.dissector (buf, pinfo, tree)
    --set name as it shows up in the protocol column
    pinfo.cols.protocol = sample_proto.name

    --our pretty delimeter
    local delim = "===================="

    --create the subtree object so we can add off of the Sample Protocol
    local subtree = tree:add(sample_proto, buf(0))

    --create a nest for just the length field
    local ln_tree = subtree:add(buf(0, 2), "Length Fields")

    --add treeitem without using protofield
    ln_tree:add(buf(0, 2), "Length: " .. buf(0,2):uint()):append_text("\t[*] add without ProtoField -- uint")

    --add treeitem without specifying endianess in both hex and int/decimal
    ln_tree:add(f_len_d, buf(0, 2)):append_text("\t[*] add with ProtoField base.DEC")
    ln_tree:add(f_len_h, buf(0, 2)):append_text("\t[*] add with ProtoField base.HEX")
    ln_tree:add_le(f_len_h, buf(0, 2)):append_text("\t[*] add_le with ProtoField base.HEX")

    --add treeitem without using protofield use le_uint() to specify little endian
    ln_tree:add(buf(0, 2), "Length: " .. buf(0, 2):le_uint()):append_text("\t[*] add without ProtoField -- le_uint")

    --add treeitem specifying little endian by using add_le
    ln_tree:add_le(f_len_d, buf(0, 2)):append_text("\t[*] add_le with ProtoField base.DEC")

    --add the delim
    subtree:add(buf(2, 1), delim .. "delim" .. delim)

    --show the transid as a base.DEC
    subtree:add(f_transid_d, buf(3, 1)):append_text("\t[*] ProtoField.uint8 base.DEC")
    subtree:add(f_transid_h, buf(3, 1)):append_text("\t[*] ProtoField.uint8 base.HEX")

    --add the delim
    subtree:add(buf(4, 1), delim .. "delim" .. delim)

    --lets display the msgtype like a string and as a uint both hex and dec
    subtree:add(f_msgtype_s, buf(5, 1)):append_text("\t[*] ProtoField.string")
    subtree:add(f_msgtype_ud, buf(5, 1)):append_text("\t[*] ProtoField.uint8 base.DEC")
    subtree:add(f_msgtype_uh, buf(5, 1)):append_text("\t[*] ProtoField.uint8 base.HEX")

    --add the delim
    subtree:add(buf(6, 1), delim .. "delim" .. delim)

    --add the msgdata
    subtree:add(f_msgdata, buf(7, 3)):append_text("\t[*] ProtoField.string")

    --add the delim
    subtree:add(buf(10, 1), delim .. "delim" .. delim)

    --display the unicode addata taking into account size of the buf
    --notice we pass in the optional value argument to ensure it is treated as unicode
    subtree:add(f_addata, buf(11, -1), buf(11, -1):ustring())

    --add addata as bytes
    subtree:add(f_addata_b, buf(11, -1))
end

--load the tcp.port tables
tcp_table = DissectorTable.get("tcp.port")

--register our protocol to handle tcp port 9999
tcp_table:add(9999, sample_proto)
