from rest_framework import serializers
from ebooks.models import Ebook



class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        exclude = ('id', 'publisher','added_at','updated_at')
        read_only_fields = ('slug',)
        
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
        else:
            files['pdf']=None
        
        if djvu:
            files['djvu']={
                "url": djvu,
                "size": instance.djvu.size
                }
        else:
            files['djvu']=None

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
        else:
            files['mobi']=None
        if doc:
            files['doc']={
                "url": doc,
                "size": instance.doc.size
                }
        else:
            files['doc']=None
        representation['files'] = files
        return representation