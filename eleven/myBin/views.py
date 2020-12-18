from django.shortcuts import render
from django.http import HttpResponse

cereals = [{'name': '100% Bran','calories': 70,'vitamins': 25,'ratings': 68.402973},
{'name': '100% Natural Bran','calories': 120,'vitamins': 0,'ratings': 33.983679},
{'name': 'All-Bran','calories': 70,'vitamins': 25,'ratings': 59.425505},
{'name': 'All-Bran with Extra Fiber','calories': 50,'vitamins': 25,'ratings': 93.704912},
{'name': 'Almond Delight','calories': 110,'vitamins': 25,'ratings': 34.384843},
{'name': 'Apple Cinnamon Cheerios','calories': 110,'vitamins': 25,'ratings': 29.509541},
{'name': 'Apple Jacks','calories': 110,'vitamins': 25,'ratings': 33.174094},
{'name': 'Basic 4','calories': 130,'vitamins': 25,'ratings': 37.038562},
{'name': 'Bran Chex','calories': 90,'vitamins': 25,'ratings': 49.120253},
{'name': 'Bran Flakes','calories': 90,'vitamins': 25,'ratings': 53.313813},
{'name': 'Cap n Crunch','calories': 120,'vitamins': 25,'ratings': 18.042851},
{'name': 'Cheerios','calories': 110,'vitamins': 25,'ratings': 50.764999},
{'name': 'Cinnamon Toast Crunch','calories': 120,'vitamins': 25,'ratings': 19.823573},
{'name': 'Clusters','calories': 110,'vitamins': 25,'ratings': 40.400208},
{'name': 'Cocoa Puffs','calories': 110,'vitamins': 25,'ratings': 22.736446},
{'name': 'Corn Chex','calories': 110,'vitamins': 25,'ratings': 41.445019},
{'name': 'Corn Flakes','calories': 100,'vitamins': 25,'ratings': 45.863324},
{'name': 'Corn Pops','calories': 110,'vitamins': 25,'ratings': 35.782791},
{'name': 'Count Chocula','calories': 110,'vitamins': 25,'ratings': 22.396513},
{'name': 'Cracklin Oat Bran','calories': 110,'vitamins': 25,'ratings': 40.448772},
{'name': 'Cream of Wheat (Quick)','calories': 100,'vitamins': 0,'ratings': 64.533816},
{'name': 'Crispix','calories': 110,'vitamins': 25,'ratings': 46.895644},
{'name': 'Crispy Wheat & Raisins','calories': 100,'vitamins': 25,'ratings': 36.176196},
{'name': 'Double Chex','calories': 100,'vitamins': 25,'ratings': 44.330856},
{'name': 'Froot Loops','calories': 110,'vitamins': 25,'ratings': 32.207582},
{'name': 'Frosted Flakes','calories': 110,'vitamins': 25,'ratings': 31.435973},
{'name': 'Frosted Mini-Wheats','calories': 100,'vitamins': 25,'ratings': 58.345141},
{'name': 'Fruit & Fibre Dates; Walnuts; and Oats','calories': 120,'vitamins': 25,'ratings': 40.917047},
{'name': 'Fruitful Bran','calories': 120,'vitamins': 25,'ratings': 41.015492},
{'name': 'Fruity Pebbles','calories': 110,'vitamins': 25,'ratings': 28.025765},
{'name': 'Golden Crisp','calories': 100,'vitamins': 25,'ratings': 35.252444},
{'name': 'Golden Grahams','calories': 110,'vitamins': 25,'ratings': 23.804043},
{'name': 'Grape Nuts Flakes','calories': 100,'vitamins': 25,'ratings': 52.076897},
{'name': 'Grape-Nuts','calories': 110,'vitamins': 25,'ratings': 53.371007},
{'name': 'Great Grains Pecan','calories': 120,'vitamins': 25,'ratings': 45.811716},
{'name': 'Honey Graham Ohs','calories': 120,'vitamins': 25,'ratings': 21.871292},
{'name': 'Honey Nut Cheerios','calories': 110,'vitamins': 25,'ratings': 31.072217},
{'name': 'Honey-comb','calories': 110,'vitamins': 25,'ratings': 28.742414},
{'name': 'Just Right Crunchy  Nuggets','calories': 110,'vitamins': 100,'ratings': 36.523683},
{'name': 'Just Right Fruit & Nut','calories': 140,'vitamins': 100,'ratings': 36.471512},
{'name': 'Kix','calories': 110,'vitamins': 25,'ratings': 39.241114},
{'name': 'Life','calories': 100,'vitamins': 25,'ratings': 45.328074},
{'name': 'Lucky Charms','calories': 110,'vitamins': 25,'ratings': 26.734515},
{'name': 'Maypo','calories': 100,'vitamins': 25,'ratings': 54.850917},
{'name': 'Muesli Raisins; Dates; & Almonds','calories': 150,'vitamins': 25,'ratings': 37.136863},
{'name': 'Muesli Raisins; Peaches; & Pecans','calories': 150,'vitamins': 25,'ratings': 34.139765},
{'name': 'Mueslix Crispy Blend','calories': 160,'vitamins': 25,'ratings': 30.313351},
{'name': 'Multi-Grain Cheerios','calories': 100,'vitamins': 25,'ratings': 40.105965},
{'name': 'Nut&Honey Crunch','calories': 120,'vitamins': 25,'ratings': 29.924285},
{'name': 'Nutri-Grain Almond-Raisin','calories': 140,'vitamins': 25,'ratings': 40.692320},
{'name': 'Nutri-grain Wheat','calories': 90,'vitamins': 25,'ratings': 59.642837},
{'name': 'Oatmeal Raisin Crisp','calories': 130,'vitamins': 25,'ratings': 30.450843},
{'name': 'Post Nat. Raisin Bran','calories': 120,'vitamins': 25,'ratings': 37.840594},
{'name': 'Product 19','calories': 100,'vitamins': 100,'ratings': 41.503540},
{'name': 'Puffed Rice','calories': 50,'vitamins': 0,'ratings': 60.756112},
{'name': 'Puffed Wheat','calories': 50,'vitamins': 0,'ratings': 63.005645},
{'name': 'Quaker Oat Squares','calories': 100,'vitamins': 25,'ratings': 49.511874},
{'name': 'Quaker Oatmeal','calories': 100,'vitamins': 0,'ratings': 50.828392},
{'name': 'Raisin Bran','calories': 120,'vitamins': 25,'ratings': 39.259197},
{'name': 'Raisin Nut Bran','calories': 100,'vitamins': 25,'ratings': 39.703400},
{'name': 'Raisin Squares','calories': 90,'vitamins': 25,'ratings': 55.333142},
{'name': 'Rice Chex','calories': 110,'vitamins': 25,'ratings': 41.998933},
{'name': 'Rice Krispies','calories': 110,'vitamins': 25,'ratings': 40.560159},
{'name': 'Shredded Wheat','calories': 80,'vitamins': 0,'ratings': 68.235885},
{'name': 'Shredded Wheat Bran','calories': 90,'vitamins': 0,'ratings': 74.472949},
{'name': 'Shredded Wheat spoon size','calories': 90,'vitamins': 0,'ratings': 72.801787},
{'name': 'Smacks','calories': 110,'vitamins': 25,'ratings': 31.230054},
{'name': 'Special K','calories': 110,'vitamins': 25,'ratings': 53.131324},
{'name': 'Strawberry Fruit Wheats','calories': 90,'vitamins': 25,'ratings': 59.363993},
{'name': 'Total Corn Flakes','calories': 110,'vitamins': 100,'ratings': 38.839746},
{'name': 'Total Raisin Bran','calories': 140,'vitamins': 100,'ratings': 28.592785},
{'name': 'Total Whole Grain','calories': 100,'vitamins': 100,'ratings': 46.658844},
{'name': 'Triples','calories': 110,'vitamins': 25,'ratings': 39.106174},
{'name': 'Trix','calories': 110,'vitamins': 25,'ratings': 27.753301},
{'name': 'Wheat Chex','calories': 100,'vitamins': 25,'ratings': 49.787445},
{'name': 'Wheaties','calories': 100,'vitamins': 25,'ratings': 51.592193},
{'name': 'Wheaties Honey Gold','calories': 110,'vitamins': 25,'ratings': 36.187559}]



def home(request):
    context = {
        'cereals' : cereals
    }
    return render(request,'myBin/home.html',context,{'title':'cereals'})

def about(request):
    return render(request,'myBin/about.html')
