from rest_framework import serializers

from e_journal.models import E_journal


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = E_journal
        fields = ('title', 'text', 'photo')