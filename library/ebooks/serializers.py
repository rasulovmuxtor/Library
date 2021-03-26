from rest_framework import serializers
from ebooks.models import Ebook

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        exclude = ('id', 'publisher')
        read_only_fields = ('publisher','slug','added_at','updated_at')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        files = {}

        pdf = representation.pop("pdf")
        djvu = representation.pop("djvu")
        epub = representation.pop("epub")
        mobi = representation.pop("mobi")
        doc = representation.pop("doc")

        if pdf:
            files['pdf']={
                "url": pdf,
                "size": instance.pdf.size
                }
        if djvu:
            files['djvu']={
                "url": djvu,
                "size": instance.djvu.size
                }
        if epub:
            files['epub']={
                "url": epub,
                "size": instance.epub.size
                }
        if mobi:
            files['mobi']={
                "url": mobi,
                "size": instance.mobi.size
                }
        if doc:
            files['doc']={
                "url": doc,
                "size": instance.doc.size
                }

        representation['files'] = files
        return representation