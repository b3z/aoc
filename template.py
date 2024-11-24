
def main(inp):
    return str(inp)




if __name__ == "__main__":
    import pyperclip as pc
    input_res = main(open('input'))
    pc.copy(input_res)
    print( '\033[34m' + main(open('test')) +  '\033[0m' + '\n\n' + input_res)

