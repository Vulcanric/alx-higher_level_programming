# 0x10. Python - Network #0
---
**`Bash`**  **`Python`**  **`Scripting`**  **`Back-end`**  **`API`**

## Learning Outcomes
The following are some of what I learnt from this project:
- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
**...**
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when I type google.com in my browser (Application level)

## Scripts and their functionality
1. [`0-body_size.sh`](https://github.com/Vulcanric/alx-higher_level_programming/blob/main/0x10-python-network_0/0-body_size.sh) takes in a URL as an argument, sends a http request to the URL, and displays the size of the response body.
2. [`1-body.sh`](https://github.com/Vulcanric/alx-higher_level_programming/blob/main/0x10-python-network_0/1-body.sh) takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response.
3. [`2-delete.sh`](https://github.com/Vulcanric/alx-higher_level_programming/blob/main/0x10-python-network_0/2-delete.sh) sends a `DELETE` request to the URL passed as the first argument and displays the body of the response.
4. [`3-methods.sh`](https://github.com/Vulcanric/alx-higher_level_programming/blob/main/0x10-python-network_0/3-methods.sh) takes in a URL and displays all HTTP methods the server will accept.
5. [`4-header.sh`](https://github.com/Vulcanric/alx-higher_level_programming/blob/main/0x10-python-network_0/0-body_size.sh) takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response. Also:
	- A header variable `X-School-User-Id` is sent with the value `98`
6. [`5-post_params.sh`](https://github.com/Vulcanric/alx-higher_level_programming/blob/main/0x10-python-network_0/5-post_params.sh) takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response.
	- A field variable `email` is sent with the value `test@gmail.com`
	- A variable `subject` is sent with the value `I will always be here for PLD`
