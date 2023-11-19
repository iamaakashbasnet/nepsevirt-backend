import csv
from django.conf import settings
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response

from v1.data.scraper.livedata import get_live_data
from v1.data.models import StockName, StockData


class LiveData(APIView):
    def get(self, request):
        get_live_data()

        with open(f'{settings.BASE_DIR}/v1/data/csv/livedata.csv', 'r', encoding='UTF-8') as file:
            reader = csv.DictReader(file)

            with transaction.atomic():
                for row in reader:
                    stock_name, created = StockName.objects.get_or_create(
                        name=row['name'])

                    stock_data, _ = StockData.objects.get_or_create(
                        name=stock_name,
                        # Defaults if doesn't exist
                        defaults={
                            'open': row['open'].replace(',', ''),
                            'high': row['high'].replace(',', ''),
                            'low': row['low'].replace(',', ''),
                            'close': row['close'].replace(',', '')
                        }
                    )

                    # Update existing entry if necessary
                    if not created:
                        stock_data.open = row['open'].replace(',', '')
                        stock_data.high = row['high'].replace(',', '')
                        stock_data.low = row['low'].replace(',', '')
                        stock_data.close = row['close'].replace(',', '')
                        stock_data.save()

        return Response({'result': 'fetched'})
