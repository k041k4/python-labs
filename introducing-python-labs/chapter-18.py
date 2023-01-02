# web examples
import urllib.request as ur

url = 'http://www.google.com'
conn = ur.urlopen(url)
print(conn.status)

data = conn.read()
print(data[:50])

#execute web browser in separate window
import webview

url = input("URL?")
webview.create_window(f"webview display of {url}", url)
