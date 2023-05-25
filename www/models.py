from django.db import models


class GameTable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    created = models.DateTimeField("date created")
    passcode = models.IntegerField()
    chips_to_dollars = models.DecimalField(max_digits=6, decimal_places=2)


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    game = models.ForeignKey(GameTable, on_delete=models.CASCADE)


class BuyIn(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(GameTable, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created = models.DateTimeField("date created")


class Winning(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(GameTable, on_delete=models.CASCADE)
    chips = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created = models.DateTimeField("date created")


class Settle(models.Model):
    created = models.DateTimeField("date created")
    game = models.ForeignKey(GameTable, on_delete=models.CASCADE)
    from_player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="from_player"
    )
    to_player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="to_player"
    )
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
