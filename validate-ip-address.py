class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        arr1 = queryIP.split('.')
        arr2 = queryIP.split(':')

        if len(arr2) == 8:
            for value in arr2:
                if 1 <= len(value) <= 4:
                    for val in value:                        
                        if val.isdigit() or "a" <= val <= "f" or "A" <= val <= "F":
                            continue
                        else:
                            return "Neither"                    
                else:
                    return "Neither"

            return "IPv6"
        elif len(arr1) == 4:
            for value in arr1:
                if value.isdigit() and 0 <= int(value) <= 255 and (len(value) == 1 or value[0] != '0'):
                    continue
                else:
                    return "Neither"

            return "IPv4"

        return 'Neither'