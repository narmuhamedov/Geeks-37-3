from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOISCES = (("rezka.ag", "rezka.ag"),)
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)

    class Meta:
        fields = [
            "media_type",
        ]

    def parser_data(self):
        if self.data["media_type"] == "rezka.ag":
            film_parser = parser.parsing()
            for i in film_parser:
                models.ParserModel.objects.create(**i)