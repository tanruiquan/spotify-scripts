<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* pip
  ```sh
    pip install python-dotenv
    pip install spotipy --upgrade
  ```

### Installation

1. Get a free API Key at [https://developer.spotify.com/dashboard/applications](https://developer.spotify.com/dashboard/applications)
2. Clone the repo
   ```sh
    git clone https://github.com/tanruiquan/spotify-scripts.git
   ```
3. Enter your API keys and playlist IDs in `.env`
   ```sh
    SPOTIPY_CLIENT_ID="YOUR SPOTIPY CLIENT ID"
    SPOTIPY_CLIENT_SECRET="YOUR SPOTIPY CLIENT SECRET"
    SPOTIPY_REDIRECT_URI="YOUR SPOTIPY REDIRECT URI"
    MY_PLAYLIST_ID="FIRST PLAYLIST ID"
    YOUR_PLAYLIST_ID="SECOND PLAYLIST ID"
    OUR_PLAYLIST_ID="NEW PLAYLIST ID"
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can run the script as such
```sh
python merge_playlist.py > temp
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>