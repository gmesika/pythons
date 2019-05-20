import docker
client = docker.from_env()
for image in client.images.list():
  #print image.id
  #print image.attrs
  d = image.attrs

  image_parent = ""
  image_repo_tags = ""
  for i in d:
      if i == "Parent":
        image_parent = d[i]
      if i == "RepoTags":
        image_repo_tags = d[i]
      #print i, d[i]
      # print i, d[i]
  if image_parent != "":
      print 'image:' + str(image.id) + ' ' + str(image_repo_tags) 
      print '\tparent: ' + image_parent
      print '\n'
  #print (', '.join(image.attrs))
