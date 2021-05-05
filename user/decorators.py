# TODO Finish or Remove
def products_page_filter(view_func):
    def wrapper(request, *args, **kwargs):
        print('Args ', args)
        print('Kwargs', kwargs)
        return view_func(request, *args, **kwargs)

    return wrapper
