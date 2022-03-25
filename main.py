from aiogram.utils import executor
from bot import dp
from hendlers import other, admin, client

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_hendler(dp)


executor.start_polling(dp, skip_updates=True)
