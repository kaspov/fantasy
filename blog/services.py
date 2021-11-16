from blog.models import Blog

def swapCreatedAndLastModified():
    for blog in Blog.objects.all():
        blog.created_at, blog.last_modified = blog.last_modified, blog.created_at
        blog.save()

