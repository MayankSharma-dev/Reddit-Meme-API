# Reddit-Meme-API
Reddit Meme API | A REST API for scrapping memes from Reddit

To fetch memes, PRAW is used to scrape memes from Reddit subreddits and return them in JSON format.
Based on Flask & PRAW.

REST API link: <a href="http://ms-reddit-memes.azurewebsites.net/about">http://ms-reddit-memes.azurewebsites.net/about

## The currently hosted API is built on FASTAPI and includes additional features, whereas this repository code represents the previous version.

It is a free and simple API, you can use it for your projects(only for educational purposes).

Note: Due to Reddit API limits and additional data filtering, the API may take some time to retrieve the scraped data. However, if requests are made less frequently, the delay can be minimized.
Please use your own authentication token. See the details at the bottom of the page.

### Default
By default the API grabs a random meme from 
"dankmemes", "memes", "HistoryMemes", "AdviceAnimals", "me_irl", "ComedyCemetery", "terriblefacebookmemes",
  "HindiMemes", "dankinindia", "IndianDankMemes", "indiameme", "ProgrammerHumor", "depression_memes", "YouSeeComrade"

Example: http://ms-reddit-memes.azurewebsites.net
Example Response:

```lua
 {
  "count": "1",
  "memes": [
    {
      "post_link": "https://redd.it/xslm2s",
      "subreddit": "memes",
      "title": "My grades start to suffer",
      "url": "https://i.redd.it/k173oxuqc4r91.jpg",
      "ups": 15,
      "nsfw": false,
      "top_comments: []",
      "author": "Flamel125",
      "image_previews": [
        "https://preview.redd.it/k173oxuqc4r91.jpg?width=108&crop=smart&auto=webp&s=e6ca586a811ea295347f56f58ca57ba449cb7d65",
        "https://preview.redd.it/k173oxuqc4r91.jpg?width=216&crop=smart&auto=webp&s=a9066370cfa9956a5513c616836a418e93aecd5d",
        "https://preview.redd.it/k173oxuqc4r91.jpg?width=320&crop=smart&auto=webp&s=4bee8223a9b4e2a2bd11683befbf0639b9738eaa",
        "https://preview.redd.it/k173oxuqc4r91.jpg?width=640&crop=smart&auto=webp&s=6251bbe89d397e1220ffc30b62516816b1630aac",
        "https://preview.redd.it/k173oxuqc4r91.jpg?width=960&crop=smart&auto=webp&s=4ed37407f2a1b73cdadf9fa0c72c3f2f2085fb75",
        "https://preview.redd.it/k173oxuqc4r91.jpg?width=1080&crop=smart&auto=webp&s=53713104f6b83441ac0b651cdad5c5361ea52478"
      ]
    }
  ]
 }
 ```

 ## Custom Endpoints
 
### Specify count (MAX 25)
In order to get multiple memes in a single request from the default subreddits, specify the count with the following endpoint.

Endpoint: /{count}

Example: https:/ms-reddit-memes.azurewebsites.net/2

Response:

```lua   
{
  "count": 2,
  "memes": [
  {
  "author": "-domi-",
  "author_img": "https://styles.redditmedia.com/t5_b0gqm/styles/profileIcon_46yo9radvx5a1.jpg?width=256&height=256&crop=256:256,smart&s=2faeea474b9d81fff0096e362669c6cd20b39fa3",
  "image_previews": [
  "https://preview.redd.it/ocaj4d4zuhdd1.png?width=108&crop=smart&auto=webp&s=f67b89b052d483101765e29e534dd4dd853ac53a",
  "https://preview.redd.it/ocaj4d4zuhdd1.png?width=216&crop=smart&auto=webp&s=b5856ead987a6fe6e49b3fe9ef3866077b64a992",
  "https://preview.redd.it/ocaj4d4zuhdd1.png?width=320&crop=smart&auto=webp&s=df40778c05c6be9e26613b3a8112255b8e35d028",
  "https://preview.redd.it/ocaj4d4zuhdd1.png?width=640&crop=smart&auto=webp&s=a6a6de88701f08953fabb332c294597b39042dfd"
  ],
  "nsfw": false,
  "post_link": "https://redd.it/1e76jz6",
  "subreddit": "ProgrammerHumor",
  "title": "loveInTimesOfOutage",
  "top_comments": [
  "Closed sauce 🍝 kernel 🌰",
  "Reminds me of the days when Microsoft bought SysInternals because those guys understood the Windows system better than Microsoft did."
  ],
  "ups": 155,
  "url": "https://i.redd.it/ocaj4d4zuhdd1.png"
  },
  {
  "author": "RhinoInsight",
  "author_img": "https://styles.redditmedia.com/t5_7rl0xu/styles/profileIcon_6idzbm91ed8b1.jpg?width=256&height=256&crop=256:256,smart&s=5b713c3d6d9f4c3db901ad90f521b7c76c53251f",
  "image_previews": [],
  "nsfw": false,
  "post_link": "https://redd.it/1d7ss7h",
  "subreddit": "programmingmemes",
  "title": "Unwrapped",
  "top_comments": [
  "Do not understand but interesting"
  ],
  "ups": 7,
  "url": "https://www.reddit.com/r/programmingmemes/comments/1d7ss7h/unwrapped/"
  }
  ]
  }
```    

### Specific Subreddit
In order to get a random posts from any subreddit, specify the subreddit name in the following endpoint.

Endpoint: /{subreddit}

Example: https:/ms-reddit-memes.azurewebsites.net/dankmemes

Response:

```lua
{
  "count": "1",
  "memes": [
    {
      "post_link": "https://redd.it/xs4lbo",
      "subreddit": "dankmemes",
      "title": "That's what friends are for",
      "url": "https://i.imgur.com/KNSmq5F.jpg",
      "ups": 157,
      "author": "NYstate",
      "nsfw": false,
      "top_comments: []",
      "image_previews": [
        "https://external-preview.redd.it/RF0EV-zxsSETT9wTVHFHrZv96paRs2DPNFVFmDZVerI.jpg?width=108&crop=smart&auto=webp&s=5988254de470417643a9e3cc12314ad723ade09c",
        "https://external-preview.redd.it/RF0EV-zxsSETT9wTVHFHrZv96paRs2DPNFVFmDZVerI.jpg?width=216&crop=smart&auto=webp&s=5aa873e41032fd5212b9d2616e82146ec7b41cc1",
        "https://external-preview.redd.it/RF0EV-zxsSETT9wTVHFHrZv96paRs2DPNFVFmDZVerI.jpg?width=320&crop=smart&auto=webp&s=922d4749c5b156339fa91e9816bd8c2bea004faa",
        "https://external-preview.redd.it/RF0EV-zxsSETT9wTVHFHrZv96paRs2DPNFVFmDZVerI.jpg?width=640&crop=smart&auto=webp&s=2f4ca0d58f8ec7b70310ecf1cb42f675c14364df",
        "https://external-preview.redd.it/RF0EV-zxsSETT9wTVHFHrZv96paRs2DPNFVFmDZVerI.jpg?width=960&crop=smart&auto=webp&s=05549083654d7d5c207d3c8ff6f6da014678721c",
        "https://external-preview.redd.it/RF0EV-zxsSETT9wTVHFHrZv96paRs2DPNFVFmDZVerI.jpg?width=1080&crop=smart&auto=webp&s=46ddec82845056b03132da2dd94ba6ac7d1f0b7f"
      ]
    }
  ]
}
```    

### Specific Subreddit & Count (MAX 25)
In order to get a custom number of posts from a specific subreddit, specify the name of the subreddit and the count in the following endpoints.

Endpoint: /{subreddit}/{count}

Example: https:/ms-reddit-memes.azurewebsites.net/memes/2

Response:
```lua
{
  "count": 2,
  "memes": [
    {
      "post_link": "https://redd.it/xsrm7o",
      "subreddit": "memes",
      "title": "This happens to me too often 😭",
      "url": "https://i.redd.it/rl3km7h356r91.jpg",
      "ups": 14,
      "author": "eric8020123",
      "nsfw": false,
      "top_comments: []",
      "image_previews": [
        "https://preview.redd.it/rl3km7h356r91.jpg?width=108&crop=smart&auto=webp&s=8aa16b4fb6cd88e89a7a00a5b92d4bc02f1b8051",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=216&crop=smart&auto=webp&s=e077c6afbda9b054e929a5762b9c5cb51b69df58",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=320&crop=smart&auto=webp&s=8ee94e542c317b5126dc1a3d3b8b96abdca4bf64",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=640&crop=smart&auto=webp&s=fc5eab35df908769246516596c7fba4ad9d369c3",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=960&crop=smart&auto=webp&s=1f697e412b09d19c75901ce2c41cb1474222d769",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=1080&crop=smart&auto=webp&s=e6d64076d0131dea73b88e16c04ddb1e3c7f04a8"
      ]
    },
    {
      "post_link": "https://redd.it/xsqsnr",
      "subreddit": "memes",
      "title": "No data about this meme",
      "url": "https://i.redd.it/8g3m7w56w5r91.png",
      "ups": 36,
      "author": "itsB0ring",
      "nsfw": false,
      "top_comments: []",
      "image_previews": [
        "https://preview.redd.it/8g3m7w56w5r91.png?width=108&crop=smart&auto=webp&s=1b956497a2901417167851c94fd6516457699f05",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=216&crop=smart&auto=webp&s=58cdd4c1e9f44d13b3fb9196a859fae36622ff2a",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=320&crop=smart&auto=webp&s=aa3f22f27402d894ddf29010d7e429341494ed0a",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=640&crop=smart&auto=webp&s=3490f9cf8846576d97c90233d423960079c548ed",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=960&crop=smart&auto=webp&s=2e35ee0e67606c7b728a13ea0e98d12ebd172af6",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=1080&crop=smart&auto=webp&s=5bbf9c34140cc2fb32130adb1245d3f6e8599a25"
      ]
    }
  ]
}
```

## With client's own auth perameters. Specific Subreddit & Count (MAX 29)

Using Client's own AUTH parameters In order to get a custom number of posts from a specific subreddit, specify the name of the subreddit and the count in the following endpoints.

Endpoint :  {client_key}/{secret_key}/{app_name}/{count}/{subreddit}/{count}

Example: https:/ms-reddit-memes.azurewebsites.net/<client_id>/<secret_key>/<app_name>/memes/2

Response :-

```lua
{
  "count": 2,
  "memes": [
    {
      "post_link": "https://redd.it/xsrm7o",
      "subreddit": "memes",
      "title": "This happens to me too often 😭",
      "url": "https://i.redd.it/rl3km7h356r91.jpg",
      "ups": 14,
      "author": "eric8020123",
      "nsfw": false,
      "top_comments: []",
      "image_previews": [
        "https://preview.redd.it/rl3km7h356r91.jpg?width=108&crop=smart&auto=webp&s=8aa16b4fb6cd88e89a7a00a5b92d4bc02f1b8051",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=216&crop=smart&auto=webp&s=e077c6afbda9b054e929a5762b9c5cb51b69df58",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=320&crop=smart&auto=webp&s=8ee94e542c317b5126dc1a3d3b8b96abdca4bf64",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=640&crop=smart&auto=webp&s=fc5eab35df908769246516596c7fba4ad9d369c3",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=960&crop=smart&auto=webp&s=1f697e412b09d19c75901ce2c41cb1474222d769",
        "https://preview.redd.it/rl3km7h356r91.jpg?width=1080&crop=smart&auto=webp&s=e6d64076d0131dea73b88e16c04ddb1e3c7f04a8"
      ]
    },
    {
      "post_link": "https://redd.it/xsqsnr",
      "subreddit": "memes",
      "title": "No data about this meme",
      "url": "https://i.redd.it/8g3m7w56w5r91.png",
      "ups": 36,
      "author": "itsB0ring",
      "nsfw": false,
      "top_comments: []",
      "image_previews": [
        "https://preview.redd.it/8g3m7w56w5r91.png?width=108&crop=smart&auto=webp&s=1b956497a2901417167851c94fd6516457699f05",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=216&crop=smart&auto=webp&s=58cdd4c1e9f44d13b3fb9196a859fae36622ff2a",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=320&crop=smart&auto=webp&s=aa3f22f27402d894ddf29010d7e429341494ed0a",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=640&crop=smart&auto=webp&s=3490f9cf8846576d97c90233d423960079c548ed",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=960&crop=smart&auto=webp&s=2e35ee0e67606c7b728a13ea0e98d12ebd172af6",
        "https://preview.redd.it/8g3m7w56w5r91.png?width=1080&crop=smart&auto=webp&s=5bbf9c34140cc2fb32130adb1245d3f6e8599a25"
      ]
    }
  ]
}
```
