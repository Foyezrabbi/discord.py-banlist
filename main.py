# @bot.hybrid_command(name="banlist", description="shows us the ban list")
@bot.command()
async def banlist(ctx):
    print("working")
    try:
      ban_list = await ctx.guild.bans()
    
      if not ban_list:
          await ctx.send("There are no banned users in this server.")
          return
      else:
          ban_list_string = ""
          for ban_entry in ban_list:
              ban_list_string += f"{ban_entry.user.name}#{ban_entry.user.discriminator}\n"
          await ctx.send(f"Here is a list of banned users in this server:\n{ban_list_string}")
    except Exception:
          await ctx.send(f"Here is a list of banned users in this server:")
