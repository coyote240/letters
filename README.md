# Letters from the Workshop

https://letters.vexingworkshop.com

This is the source for my blog, [Letters from the
Workshop](https://letters.vexingworkshop.com). The site is generated using the
Pelican static site generator, which reduces the friction encountered when
writing while eliminating the need to expend cycles maintaining a database. If
the content is static, why not deliver static content?

The theme is derived from the default 'notmyidea' theme that ships with Pelican.

All content on this site, unless otherwise specified, is licenced under a
[Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/)

## Developing Locally

```shell
pelican -r --listen content
```

## Testing Using Docker

### Build the image

```shell
docker build -t vexingworkshop/letters:latest
```


### Run the image

```shell
docker run --rm -p 8080:80 vexingworkshop/letters
```
