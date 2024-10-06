# import os
#
# import pdoc
#
# modules = ['CustomLibTemplate']  # Public submodules are auto-imported
# context = pdoc.Context()
#
# modules = [pdoc.Module(mod, context=context)
#            for mod in modules]
# pdoc.link_inheritance(context)
#
# def recursive_htmls(mod):
#     yield mod.name, mod.html()
#     for submod in mod.submodules():
#         yield from recursive_htmls(submod)
#
# for mod in modules:
#     for module_name, html in recursive_htmls(mod):
#         with open(os.path.join('docs', f"{module_name}.html"), 'w') as file:
#             file.write(html)



def read_requirements():
    """
    Read requirements.txt and return it as list of dependencies.
    """
    with open ('requirements.txt', 'r') as file:
        return file.read().split('\n')

print(read_requirements())