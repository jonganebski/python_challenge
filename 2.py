p = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
alphabet = "abcdefghijklmnopqrstuvwxyz"
answer = ""
for i in p:
  if i >= alphabet:
    nindex = alphabet.index(i) + 2
    if nindex > 25:
      nindex -= 26
    answer += alphabet[nindex]
  else:
    answer += i
print(answer)
