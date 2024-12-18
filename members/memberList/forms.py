from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    members = forms.CharField(
        widget=forms.Textarea,
        required=False,
        help_text="Enter each member on a new line, with name, post, and shares separated by commas.",
    )

    class Meta:
        model = Contract
        fields = ["title", "members", "comment"]

    def clean_members(self):
        members_data = self.cleaned_data["members"]
        members_list = []
        if members_data:
            for member in members_data.split("\n"):
                parts = member.split("-")
                if len(parts) < 2:
                    raise forms.ValidationError(
                        "Each member must have at least a name and a post, separated by commas."
                    )
                name = parts[0].strip()
                post = parts[1].strip()
                shares = parts[2].strip() if len(parts) > 2 else ""
                members_list.append(f"{name}-{post}-{shares}")
        return "\n".join(members_list)
