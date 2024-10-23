"""
<one line to give the program's name and a brief idea of what it does.>
Copyright (C) 2024 ItsAsheer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import nextcord # use import nextcord for v1.2
from nextcord.ext import commands
import os
import fcntl

# File to store the call count
count_file = "call_count.txt"

def record_function_call():
    # Open the file in read-write mode, or create it if it doesn't exist
    with open(count_file, 'a+') as f:
        # Lock the file to prevent race conditions
        fcntl.flock(f, fcntl.LOCK_EX)
        
        # Move to the start of the file to read the count
        f.seek(0)
        content = f.read().strip()
        
        # If file is empty, initialize count to 0
        if not content:
            count = 0
        else:
            count = int(content)
        
        # Increment the count
        count += 1
        
        # Move back to the start and write the new count
        f.seek(0)
        f.write(str(count))
        f.truncate() # Ensure any leftover data is removed
        
        # Unlock the file
        fcntl.flock(f, fcntl.LOCK_UN)

class Template(commands.Cog):
    """A template cog written for unifier-plugin temmplate repo"""
    
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def template(self,ctx):
        await ctx.send('This is a template plugin!')
        
    async def process(message):
        record_function_call()
        return message

def setup(bot):
    bot.add_cog(Template(bot))
