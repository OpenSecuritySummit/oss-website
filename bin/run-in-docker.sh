#HUGO_VERSION=0.91.2
HUGO_VERSION=0.93.2

# need to use {$version}ext-alpine because it has the git executable
docker run -v $PWD:/src -p 1313:1313 --rm -it klakegg/hugo:${HUGO_VERSION}-ext-alpine serve