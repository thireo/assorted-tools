#!/bin/sh

repo_name=$1
token=7ASjNEZ_YWUPHabbRp75

test -z $repo_name && echo "Repo name required." 1>&2 && exit 1
echo $repo_name
curl -H "Content-Type:application/json" -H "PRIVATE-TOKEN: $token" -X POST -d "{\"name\": \"$repo_name\",\"namespace_id\":\"3\"}" http://192.168.0.6:30000/api/v4/projects
