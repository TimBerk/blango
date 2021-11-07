from django import template
from django.contrib.auth import get_user_model
from django.utils.html import format_html


User = get_user_model()
register = template.Library()


@register.filter
def author_details(author, current_user=None):
  if not isinstance(author, User):
    return ""
  
  if author == current_user:
    return format_html("<strong>me</strong>")

  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"

  if author.email:
    prefix = format_html(f'<a href="mailto:{author.email}">')
    suffix = format_html("</a>")
  else:
    prefix = ""
    suffix = ""

  return format_html(f'{prefix}{name}{suffix}')
