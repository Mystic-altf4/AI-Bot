import discord
from discord.ext import commands
import k

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f"Selam {ctx.author}. Ben {bot.user}")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya.save(f"resim/{dosya.filename}")
            await ctx.send("Resim Kaydedildi")
        sinif,skor =  k.bot(f"resim/{dosya.filename}")
        if sinif == "Spike\n":
            await ctx.send("Spike")
            await ctx.send("Çoğu insan Spike'ın Ranger Çiftliği'nde Colt ve Shelly'nin sevimli yardımcısı olduğunu düşünüyor. Hiç kimse onun travmasının derinliğini tahmin edemez")
            await ctx.send("<:indir15:1269570409930428519>")
        elif sinif == "Draco\n":
            await ctx.send("Draco")
            await ctx.send("Şişme ejderhasına binip havai fişekler patlatan Draco, her gece göz kamaştırıcı bir final vadediyor. Elektro gitarı gürleyerek ve alev saçan yolculuğu kalabalığı sarsarak fanteziyi on bire çıkarıyor!")
            await ctx.send("<:indir15:1269570409930428519>")
        elif sinif == "Rico\n":
            await ctx.send("Rico")
            await ctx.send("Rico kesinlikle galaksinin en çok aranan suçlularını takip eden gerçek bir uzay ödül avcısı, havalıymış gibi davranan bir sakız makinesi değil.")        
            await ctx.send("<:indir15:1269570409930428519>")
        elif sinif == "Melodie\n":
            await ctx.send("Melodie")
            await ctx.send("Karaoke söz konusu olduğunda Melodie hiç merhamet göstermiyor. Sevimli görünümü ve şeytani düdüğüyle, ilgi odağı olmayı her zaman başarıyor.")
            await ctx.send("<:indir15:1269570409930428519>")
        elif sinif == "Srank\n":
            await ctx.send("Srank")
            await ctx.send("Srank gündüzleri morgda yardım eden ve geceleri Kulüpte müzik çalan iyi huylu bir dev. Çok fazla uyumuyor ve bu belli oluyor.")
            await ctx.send("<:indir15:1269570409930428519>")
        elif sinif == "Lily\n":
            await ctx.send("Lily")
            await ctx.send("Özünde bir inek ve tam bir büyücülük tutkunu olan Lily'nin bilgiye olan açlığı onu bir zamanlar Büyülü Orman'a sürükledi ve burada bir ateş böceği ve etçil bir bitkinin karıştığı bir olay hayatını sonsuza dek değiştirecekti...")  
            await ctx.send("<:indir15:1269570409930428519>")
        elif sinif == "Tick\n":
            await ctx.send("Tick")
            await ctx.send("Tick, Penny'nin bir sonraki büyük planını planlarken onu bir evcil hayvan gibi takip ediyor. Bir şeyleri havaya uçurmaktan başka pek bir işe yaramıyor ama genelde bu da yeterli oluyor!")
            await ctx.send("<:indir15:1269570409930428519>")
        elif sinif == "edgay\n"  :
            await ctx.send("edgay")
            await ctx.send("Edgay kimsenin onu anlamadığına inanıyor. Özellikle de bir evreden geçtiğini düşünen annesi. Ruhundaki karanlığın sonsuz olduğunu yalnızca o biliyor.")
            await ctx.send("<:indir15:1269570409930428519>")
        elif sinif == "eternxlkz\n":
            await ctx.send("eternxlkz")
            await ctx.send("Phonk üreticisi. Popüler Şarkıları: SLAY!, ENOUGH!, DRESS!, PHARAOH!")
            await ctx.send("<:indir15:1269570409930428519>")
        elif sinif == "other\n":
            await ctx.send("Bilmem")  
            await ctx.send("<:indir21:1269567957751693404>")          
            await ctx.send("<:indir22:1269567940156457021>")
            await ctx.send("<:indir31:1269567917490442270>")
            await ctx.send("<:indir12:1269567893897613342>")
    else:
        await ctx.send("Resim Göndermediniz")
bot.run("TOKEN")
