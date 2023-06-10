from Svelte_Web.services.products_service import get_all_category


def all_categories(request):
    categories = get_all_category() 
    print(categories)
    return {"categories": categories}