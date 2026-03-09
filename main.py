from telethon import TelegramClient, events

api_id = 32119175
api_hash = "deeebb02fdf5bba8873dbebb79bfce74"

origem = -1001720188500   # canal/grupo que será monitorado
destino = -1003849014399  # grupo que vai receber os vídeos

client = TelegramClient("baixador", api_id, api_hash)

@client.on(events.NewMessage(chats=origem))
async def handler(event):

    if event.video:
        print("Video detectado")

        caminho = await event.download_media()

        print("Enviando sem legenda...")

        await client.send_file(
            destino,
            caminho,
            caption=None
        )

client.start()
print("Bot rodando...")
client.run_until_disconnected()
