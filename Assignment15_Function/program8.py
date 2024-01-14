def outer():
    message="I am the outer Function."
    def inner():
        return message
    return inner
if __name__=='__main__':
    inner_function=outer()
    result = inner_function()
    print(result)

# Output
    # I am the outer Function.