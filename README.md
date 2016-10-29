Those are the files used to generate my blog. Since I keep forgetting how to use pelican, here is the short guide:

1. Add some content to `content/articles`.
1. Run:

	```sh
		pelican content
	```
1. Check if everything looks ok by running the local server:

	```sh
		cd output/ && python -m pelican.server
	```
1. Publish the post by adding the files, commiting and pushing from `output`. 
1. Push the sources


## TODO:
* Add [post statistics](https://github.com/getpelican/pelican-plugins/tree/master/post_stats) support
* Define a nicer [formatting style](http://www.christianlong.com/blog/more-on-pelican-themes.html) for code
* Use [git-hooks](http://docs.getpelican.com/en/3.6.3/tips.html#extra-tips) to publish content automatically when commiting new source changes
* Add a plugin to [embed videos](http://docs.getpelican.com/en/3.6.3/tips.html#how-to-add-youtube-or-vimeo-videos)
