Those are the files used to generate my blog. Since I keep forgetting how to use pelican, here is the short guide:

1. Add some content to `content/articles`.
2. Run

```sh
	pelican content
```

3. Check if everything looks ok by running the local server:

```sh
	cd output/ && python -m pelican.server
```

4. Publish the post by adding the files, commiting and pushing from `output`. 
5. Push the sources


