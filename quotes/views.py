# File: views.py
# Author: Gab Alingog (galingog@bu.edu), 09/14/2026
# Description: Stores the quotes and images utilized by the website, alongside the primary functions.

from django.shortcuts import render
import random

# Stores all the Spider-Man quotes used
quotes = ["I'm just your friendly neighborhood Spider-Man",
            "What is the point of having some kind of special power if you don't use it to help people?",
            "Sometimes to do what's right we must be steady and give up the things we desire the most… even our dreams.",
              "It's a leap of faith. That's all it is, Miles. A leap of faith.",
              "When you think you've given your all… When you think you can't keep going… Spider-Man always gets up.",
              "I'd rather just stay on the ground for a little while. Friendly neighborhood Spider-Man. Somebody's got to look out for the little guy, right?",
              "When you can do the things I can, but you don’t, and then the bad things happen... they happen because of you.",
              "I-I got... homework.",
              "That you're wrong. You think you're right. And that makes you dangerous.",
              "This is my chance to prove myself.",
              "New York. Queens. It's a rough borough, but, hey, it's home.",
              "Just because we've lost someone... It doesn't mean we have to do this alone. I mean we can't. Trust me, I've been trying. It doesn't work.",
              "You have me.",
              "Because I'm not just Peter Parker. I'm Spider-Man. And sometimes Spider-Man has to do the hard thing, even if it breaks Peter Parker's heart.",
              ]

# Stores all the Spider-Man images used
images = ["https://variety.com/wp-content/uploads/2015/02/spidey.jpg?w=1000&h=667&crop=1",
               "https://cdn.mos.cms.futurecdn.net/3JCaEkiSwWKAwgLMjpChF3-1200-80.jpg",
               "https://static0.polygonimages.com/wordpress/wp-content/uploads/2026/08/spider-man-brand-new-day-tom-holland.jpg?w=1600&h=900&fit=crop",
               "https://cdn.britannica.com/54/93454-050-5AC49E5E/Spider-Man-Tobey-Maguire-2.jpg",
               "https://c.files.bbci.co.uk/416d/live/ee8f50b0-8c2e-11f1-9fe2-97492b603d93.jpg",
               "https://assets-prd.ignimgs.com/2026/08/03/peter-spidey-deck-blogroll-1785792270027.jpg",
               "https://bloximages.chicago2.vip.townnews.com/thestar.com/content/tncms/assets/v3/editorial/c/26/c265f4cb-83d5-5f3c-86ba-8f3be2d35d35/6a6fca8aadbc6.image.jpg?resize=1200%2C800",
               "https://variety.com/wp-content/uploads/2021/12/Spider-Man-2.jpg?w=800",
               "https://m.media-amazon.com/images/M/MV5BMjIxNDc5MDM4Ml5BMl5BanBnXkFtZTcwNTM3OTMwOA@@._V1_.jpg",
               "https://media.philstar.com/photos/2023/05/31/spider-man-across-spider-verse_2023-05-31_23-31-37.jpg",
               "https://variety.com/wp-content/uploads/2026/08/MCDSPMA_CO021_6c0074.jpg?w=1000&h=562&crop=1",
               "https://static01.nyt.com/images/2019/06/27/arts/spiderman1/spiderman1-superJumbo.jpg",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJL2ECcV5jIKXVjmYj-F69NL4Re6zSjfPmZBhFHWQKu_wooUJLHYQkwtU&s=10",
               "https://images.immediate.co.uk/production/volatile/sites/3/2017/06/142032.793e80d3-3e80-48de-b26e-c2a26c3e42fe.jpg",
               "https://a.ltrbxd.com/resized/sm/upload/lb/g8/9t/dr/spider-man-homecoming-1200-1200-675-675-crop-000000.jpg?v=a0c830f403",
               "https://static01.nyt.com/images/2017/06/30/arts/07SPIDERMAN2/07SPIDERMAN2-superJumbo.jpg",
               ]

# Functions to create a quote of the day website

def main(request):
    """Direct the logic to the quote function since the path specificed to main"""
    return quote(request)

def quote(request):
    """Displays a random quote and image to the page"""

    # Picks a random quote and image
    rand_quote = random.randint(0, len(quotes) - 1)
    rand_img = random.randint(0, len(images) - 1)
    context = {
        'quote': quotes[rand_quote],
        'image': images[rand_img],
    }
    template_name = 'quotes/quote.html'
    return render(request, template_name, context)

def show_all(request):
    """Displays all the quote and image data"""

    # Returns every data in the list
    context = {
        'quotes': quotes,
        'images': images,
    }
    template_name = 'quotes/show_all.html'
    return render(request, template_name, context)

def about(request):
    """Displays a short biographical information about the person in the images"""
    template_name = 'quotes/about.html'
    return render(request, template_name)