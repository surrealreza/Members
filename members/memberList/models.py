from django.db import models


class Contract(models.Model):
    title = models.CharField(max_length=200)
    members = models.TextField(blank=True)
    comment = comment = models.TextField(null=True)

    def __str__(self):
        return self.title

    def get_members(self):
        members_list = []
        if self.members:
            for member in self.members.split("\n"):
                parts = member.split("-")
                name = parts[0].strip()
                post = parts[1].strip() if len(parts) > 1 else ""
                shares = parts[2].strip() if len(parts) > 2 else ""
                members_list.append({"name": name, "post": post, "shares": shares})
        return members_list

    def get_comment(self):
        if not isinstance(self.comment, str):
            return []

        words = self.comment.split()
        lines = []
        current_line = ""
        line_length = 0

        for word in words:
            if line_length + len(word) + 1 > 50:
                lines.append(current_line)
                current_line = word
                line_length = len(word)
            else:
                if line_length > 0:
                    current_line += " "
                    line_length += 1
                current_line += word
                line_length += len(word)

        if current_line:
            lines.append(current_line)

        return lines
