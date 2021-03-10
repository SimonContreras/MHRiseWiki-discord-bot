import os
import sys
sys.path.insert(0,os.getcwd())
import unittest
from unittest.mock import MagicMock, patch
from discord import Embed, Emoji
from discord.ext import commands

from src.armor.embed import ArmorEmbed
from src.common.embed import CommonEmbed
from src.error.embed import ErrorEmbed
from src.help.embed import HelpEmbed
from src.item.embed import ItemEmbed
from src.language.embed import LanguageEmbed
from src.monster.embed import MonsterEmbed
from src.prefix.embed import PrefixEmbed
from src.skill.embed import SkillEmbed
from src.weapon.embed import WeaponEmbed
from serialize_mocks import *

from src.orm.models import *

class TestEmbeds(unittest.TestCase):

    def test_armor_embed(self):
        dct = armor_dct
        headers = armor_headers
        e = ArmorEmbed(dct, headers)
        main = e.main()
        details = e.details(0)
        self.assertIsInstance(main, Embed)
        self.assertIsInstance(details, Embed)
    
    @patch('__main__.Header', autospec=Header)
    def test_common_embed_not_found(self, footer_mock):
        dct = not_found_dct
        footer_mock.name = 'footer_eng'
        footer_mock.translation = 'Escribe {prefix} ayuda para más info en algún comando'
        footer_mock.type = 'general_footer'
        ctx = MagicMock(prefix='!')
        e = CommonEmbed(dct, footer_mock, ctx)
        self.assertIsInstance(e.notFound(), Embed)
    
    @patch('__main__.Header', autospec=Header)
    @patch('__main__.Header', autospec=Header)
    @patch('__main__.Header', autospec=Header)
    @patch('__main__.commands.Context', autospec=commands.Context)
    def test_error_embed_3_possibles_msg(self, h1_mock, h2_mock, h3_mock, ctx_mock):
        h1_mock.name = 'mock1'
        h1_mock.type = 'disabled_command'
        h1_mock.translation = '''test text {command}'''
        h2_mock.name = 'mock2'
        h2_mock.type = 'missing_required_argument'
        h2_mock.translation = 'Falta el argumento **{params}** para el comando **{prefix}{command}**.'
        h3_mock.name = 'mock3'
        h3_mock.type = 'another error'
        h3_mock.translation = 'default message error'
         
        ctx_mock.command = 'armor'
        ctx_mock.invoked_with = 'armor_esp'
        ctx_mock.prefix = '!'

        e_1 = ErrorEmbed(h1_mock, ctx_mock)
        e_2 = ErrorEmbed(h2_mock, ctx_mock)
        e_3 = ErrorEmbed(h3_mock, ctx_mock)
        self.assertIsInstance(e_1.main(), Embed)
        self.assertIsInstance(e_2.main(), Embed)
        self.assertIsInstance(e_3.main(), Embed)

    def test_help_embed(self):
        ctx = MagicMock(prefix='!')
        dct = help_dct
        e = HelpEmbed(ctx, dct)
        self.assertIsInstance(e.main(), Embed)

    def test_item_embed(self): 
        dct = item_dct
        headers = item_headers     
        e = ItemEmbed(dct, headers)
        self.assertIsInstance(e.main(), Embed)

    @patch('__main__.Header', autospec=Header)
    @patch('__main__.Header', autospec=Header)
    def test_language_embed(self, h1_mock, h2_mock):
        h1_mock.name = 'Notification'
        h1_mock.type = 'language_changed'
        h1_mock.translation = 'Language changed to {new_lang}'
        h2_mock.name = 'Notification test'
        h2_mock.type = 'language_not_supported'
        h2_mock.translation = 'Language not supported.'

        # Language changed
        e_1 = LanguageEmbed(h1_mock, 'esp')
        self.assertIsInstance(e_1.main(), Embed)
        # Language didn't change
        e_2 = LanguageEmbed(h2_mock, None)
        self.assertIsInstance(e_2.main(), Embed)
    
    def test_monster_embed(self):
        dct = monster_dct
        headers = monster_headers
        e = MonsterEmbed(dct, headers)
        m_1, m_2 = e.main()
        d_1, d_2 = e.details()
        self.assertIsInstance(m_1, Embed)
        self.assertIsInstance(m_2, Embed)
        self.assertIsInstance(d_1, Embed)
        self.assertIsInstance(d_2, Embed)
        
    def test_prefix_embed(self):
        h_1 = MagicMock(
            name='Notification test',
            translation=f'''El $prefix no puede ser utilizado, largo mayor a 3.''',
            type='prefix_cant_be_change'
        )
        h_2 = MagicMock(
            name='Notification test',
            translation=f'''Prefix changed succesfully to $new_prefix.''',
            type='prefix_change_succesfully'
        )
        e_1 = PrefixEmbed(h_1,'!!!!!')
        e_2 = PrefixEmbed(h_2,'!')
        # Wrong prefix
        self.assertIsInstance(e_1.main(), Embed)
        # Correct prefix
        self.assertIsInstance(e_2.main(), Embed)

    def test_skill_embed(self):
        dct = skill_dct
        headers = skill_headers
        e = SkillEmbed(dct, headers)
        self.assertIsInstance(e.main(), Embed)

    @patch('__main__.Emoji', autospec=Emoji)
    @patch('__main__.Emoji', autospec=Emoji)
    def test_weapon_embed(self, emoji1_mock, emoji2_mock):
        emoji1_mock.name = 'lbg'
        emoji1_mock.id = 1
        emoji1_mock.is_usable = MagicMock(return_value=True)
        emoji2_mock.name = 'ls'
        emoji2_mock.id = 2
        emoji2_mock.is_usable = MagicMock(return_value=True)

        guild_mock = MagicMock(
            emojis = [emoji1_mock, emoji2_mock]
        )
        
        ctx = MagicMock(
            guild = guild_mock
        )
        dct = weapon_dct
        headers = weapon_headers
        e = WeaponEmbed(dct, ctx, headers)
        self.assertIsInstance(e.main(), Embed)

if __name__ == '__main__':
    unittest.main()




