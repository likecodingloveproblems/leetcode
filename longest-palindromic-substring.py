from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        biggest_string = s[0]
        centeral_index = 0
        sub = deque()
        while True:
            radius = 1
            while True:
                left_index = centeral_index - radius
                right_index = centeral_index + radius
                if left_index < 0 or right_index >= len(s):
                    break
                elif s[left_index] == s[right_index]:
                    if radius == 1:
                        sub = deque(s[centeral_index])
                    sub.append(s[right_index])
                    sub.appendleft(s[left_index])
                    radius += 1
                else:
                    break

            if len(sub) > len(biggest_string):
                biggest_string = "".join(sub)

            radius = 0
            while True:
                left_index = centeral_index - radius
                right_index = centeral_index + radius + 1
                if left_index < 0 or right_index >= len(s):
                    break
                elif s[left_index] == s[right_index]:
                    if radius == 0:
                        sub = deque()
                    sub.append(s[right_index])
                    sub.appendleft(s[left_index])
                    radius += 1
                else:
                    break

            if len(sub) > len(biggest_string):
                biggest_string = "".join(sub)

            centeral_index += 1
            if centeral_index >= len(s):
                break

        return biggest_string


if __name__ == "__main__":
    import time

    t1 = time.time()
    solution = Solution().longestPalindrome(
        # "baabx"
        # "babad"
        # "cstgvkbrxacmpxdxxktktvpdzcuxmnhvuxdgsmskgeeawzeikhtmhdvnccbrgifpzmiuytfmeyfoxsntrdtxeuxcqsndexbgfxnthqwveujqzemloooyddparbjcuiwpopjwvvmwblsamkhjhlnoxinkpsempexmipifsfwzxbetgvfnkngzxcpizwctpdlpngjpyovmjllxfiwktghkxvyelwjwdztujmunijfsfdvmhgqhlpouewgyznphlmccjmqaqncwbeqheohibafqfunfywmrvqvjygjwqoclijwkcfiuaiymeagdbwyejnvtosxylptbtyoahfzfmwzrkhzdamknleroffmsqcaryibamgdpcumlhrblypddzhaxfeztokgogzgvpfvlmetiwsamhdidmvxavleryfyakendwrbslcavlqkerrnvpuzhdgwzuyorxzbkzhxhpbvkflgxouvaavxrdzsjlgrmogzvlhhdidldsxqhrqlryaanffhxnutcycnczuedtrwcnfiqrtoafvdfnfhxhyjivzalozrbrajboecfyalisxxanduzraqdrbzsbkobaieqpzcawrunxucypqyjnmrlrlivrrwwhdpekeelsphhunzbhkkejvqfopjsuholutgmtnleqdrntbqgrobnuhqpdkbjtikijkdiwqvnxgajaaqgswrdamzv"
    )
    t2 = time.time()
    print(solution)
    print(t2 - t1)
