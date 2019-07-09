from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[
    {
    "restaurant_name":"Babel",
    "food_type":"Lebanese"
    },
    {
    "restaurant_name":"wok and roll",
    "food_type":"Japanese"
    },
    {
    "restaurant_name":"Hardees",
    "food_type":"Fast food"
    }
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{ "restaurant_name":"chilies", "food_type":"american"

    }
    }
    return render(request, 'detail.html', context)
