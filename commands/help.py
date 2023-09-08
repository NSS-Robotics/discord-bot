import interactions

GUILD_IDS = [918591198799749240]


class Help(interactions.Extension):
    def __init__(self, bot: interactions.Client) -> None:
        self.bot = bot

    @interactions.slash_command(name="help", description="Lists available commands")
    async def help(self, ctx) -> None:
        embed = interactions.Embed(title="Help")
        embed.add_field(
            name="Annoy Someone",
            value="`/annoy` \n Pings a given user a specified number of times. Only works for <@&918640986618486794>'s <@&918638863516328056>'s & <@&962812802840539136>'s",
            inline=False,
        )
        embed.add_field(
            name="Ping",
            value="`/ping` \n Shows <@963255439963869244>'s latency",
            inline=False,
        )
        embed.add_field(
            name="Playlist Link",
            value="`/playlist` \n Sends the link to the robotics Spotify playlist",
            inline=False,
        )
        embed.add_field(
            name="Media Link",
            value="`/media` \n Sends an embed with the link to the Google Drive folder with all the photos",
            inline=False,
        )
        await ctx.send(embeds=embed, ephemeral=True)


def setup(bot: interactions.Client) -> None:
    Help(bot)
