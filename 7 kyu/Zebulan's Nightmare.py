def zebulans_nightmare(function):
    function = function.split("_")
    for i in range(1,len(function)):
        function[i] = function[i].capitalize()
    return ''.join(function)