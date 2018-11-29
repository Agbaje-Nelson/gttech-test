# On this day, Nov 29, 2018, scrape the https://punchng.com/ sections as listed below
# 1. JUST IN
# 2. TRENDING
# Return the output as a JSON in Javascript



# PUNCH EXTRACTION
# JUST-IN LIST

let Justin = document.querySelectorAll('h3');
let response = {};

for (let count = 0; count < Justin.length; count ++){
    response[count] = Justin[count].textContent;
    }
    document.write(JSON.stringify(response));


# TRENDING LIST


let Trending = document.querySelectorAll('span.tptn_after_thumb');
let response = {};

for (let count = 0; count < Trending.length; count ++){
    response[count] = Trending[count].textContent;
    }
    document.write(JSON.stringify(response));