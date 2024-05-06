from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from django_select2.forms import Select2MultipleWidget
from django import forms

from assets.models import Asset
from cves.models import Vendor
from cves.models import Product

class AssetForm(forms.ModelForm):
    vendor = forms.ModelMultipleChoiceField(
        queryset=Vendor.objects.all(),
        widget=Select2MultipleWidget,
    )

    class Meta:
        model = Asset
        fields = ["name", "description", "vendor", "product", "version"]

    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Add an asset",
                "name",
                "description",
                "product",
                "version",
                "vendor"
            ),
            Submit("submit", "Add asset"),
        )
