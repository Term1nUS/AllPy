class Solution:
    def reverse(self, x: int) -> int:
        mul = 1
        rev_int = 0
        result = 0
        if -2**31 <= x <= 2**31 - 1:
            if x < 0:
                mul = -1
                x *= -1
            rev_int = str(x)[::-1]
        if -2**31 <= int(rev_int) <= 2**31 - 1:
            result = int(rev_int)
        return result*mul

    def myAtoi(self, s: str) -> int:
        res_str = s.strip()
        idx_from = 0
        mul = 1
        if len(res_str) > 0:
            if res_str[0] == "+" and len(res_str) > 1:
                mul = 1
                idx_from = 1
            else:
                pre_res = 0
            if res_str[0] == "-" and len(res_str) > 1:
                mul = -1
                idx_from = 1
            else:
                pre_res = 0
            if res_str[idx_from].isdigit():
                i = idx_from
                mid_str = ""
                while i < len(res_str):
                    if res_str[i].isdigit():
                        mid_str += res_str[i]
                        i += 1
                    else:
                        break
                pre_res = int(mid_str)*mul
            else:
                pre_res = 0
        else:
            pre_res = 0
        if pre_res > 2**31 - 1:
            pre_res = 2**31 - 1
        elif pre_res < -2**31:
            pre_res = -2**31
        return pre_res

    def areNumbersAscending(self, s: str) -> bool:
        s = s.strip()
        if 200 >= len(s) >= 0:
            i = 0
            str = ""
            while i < len(s):
                if s[i] == " " or s[i].isdigit():
                    str += s[i]
                i += 1
            prev_len = len(str)
            changed = True
            while changed:
                x = str.replace("  ", " ")
                str = x
                if len(x) != prev_len:
                    prev_len = len(x)
                    changed = True
#                    print(x)
                else:
                    changed = False
            list = str.split()
            if 100 >= len(list) >= 2:
                prev_x = list[0]
                asc = True
                for i in range(1, len(list)):
                    if int(list[i]) > int(prev_x):
                        prev_x = list[i]
                    else:
                        asc = False
            else:
                asc = False
        return asc

    def checkString(self, s: str) -> bool:
        if 100 >= len(s) >= 2:
            order = True
            ch = 0
            prev = "a"
            for i in range(0, len(s)):
                if s[i] != prev:
                    ch += 1
                    if prev == "b":
                        prev = "a"
                    else:
                        prev = "b"
            if ch > 1:
                order = False
        elif len(s) == 1:
            order = True
        return order


s = Solution()

print(s.checkString("abaabbb"))
print(s.checkString("abab"))
print(s.checkString("bbb"))


