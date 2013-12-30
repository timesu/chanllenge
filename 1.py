import string

original = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
              rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl
              zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
              sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

table = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab"
)

password = string.maketrans(
    string.ascii_lowercase,
    string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
)

key = "map"

#print original.translate(table)
#print key.translate(table)

print string.translate(original,password)