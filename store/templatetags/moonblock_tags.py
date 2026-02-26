from django import template

register = template.Library()


@register.filter
def t(obj, lang):
    """Get translated field: {{ product|t:lang }} uses product.name(lang)"""
    if callable(getattr(obj, 'name', None)):
        # For objects with name(lang) method — used as {{ product|t:lang }}
        return obj.name(lang)
    return obj


@register.simple_tag
def trans(obj, field, lang):
    """{% trans obj 'title' lang %} — calls obj.title(lang)"""
    method = getattr(obj, field, None)
    if callable(method):
        return method(lang)
    return getattr(obj, f'{field}_{lang}', '') or getattr(obj, f'{field}_en', '')


@register.simple_tag
def site_t(site, field, lang):
    """{% site_t site 'hero_eyebrow' lang %}"""
    return site.t(field, lang)


@register.filter
def split(value, delimiter=','):
    return value.split(delimiter)


@register.simple_tag
def lang_url(request, target_lang):
    """Return URL with lang param."""
    params = request.GET.copy()
    params['lang'] = target_lang
    return '?' + params.urlencode()
