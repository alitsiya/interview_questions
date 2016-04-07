# Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.

def rev(string):

    def _rev(pos, res_str):
        if pos >= len(string):
            return "".join(res_str)
        res_str.append(string[len(string)-pos-1])
        return _rev(pos+1, res_str)

    return _rev(0, [])

print rev('abcdef')

#This older implimentation is bad since we trim original string every time
# def rev(string):
#     if len(string) <= 1:
#         return string
#     return rev(string[1:]) + string[0]
