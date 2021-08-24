#from django.urls import resolve
from BMIList.models import Item, unit
from django.test import TestCase
#from BMIList.views import BmiPage
#from django.http import HttpRequest 
class BmiPageTest(TestCase):
	def test_uses_template(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'bmi.html')
	

class ORMTest(TestCase):

	def test_saveretrievelist(self):
		newPiece = unit()
		newPiece.save()
		txtItem1=Item()
		txtItem1.text='item one'
		txtItem1.KeyId = newPiece
		txtItem1.save()
		txtItem2=Item()
		txtItem2.KeyId = newPiece
		txtItem2.text='item two'
		txtItem2.save()
		saved_Items=Item.objects.all()
		savedunit = unit.objects.first()
		self.assertEqual(saved_Items.count(),2)
#		self.assertEqual(savedunit.newPiece)
		savedItem1=saved_Items[0]
		savedItem2=saved_Items[1]
		self.assertEqual(txtItem1.text, 'item one')
		self.assertEqual(txtItem2.text, 'item two')
		self.assertEqual(txtItem1.KeyId, newPiece)
		self.assertEqual(txtItem2.KeyId, newPiece)
		
	
class ViewTest(TestCase):
		
	def test_displays_all(self):
		newunit = unit.objects.create()
		Item.objects.create(KeyId=newunit, text='GelynRica')
		Item.objects.create(KeyId=newunit, text='DanielleMilleth')
		response = self.client.get(f'/BMIList/{newunit.id}/')
		self.assertContains(response,'GelynRica')
		self.assertContains(response,'DanielleMilleth')
		self.assertNotContains(response,'Sir Dong')
		self.assertNotContains(response,'Papasa')
		
		newunit_2 = unit.objects.create()
		Item.objects.create(KeyId=newunit_2, text='Sir Dong')
		Item.objects.create(KeyId=newunit_2, text='Papasa')
		response = self.client.get(f'/BMIList/{newunit_2.id}/')
		self.assertContains(response,'Sir Dong')
		self.assertContains(response,'Papasa')
		self.assertNotContains(response,'GelynRica')
		self.assertNotContains(response,'DanielleMilleth')
		
	def test_listview_gumamitng_listpage(self):
		newunit = unit.objects.create()
		response = self.client.get(f'/BMIList/{newunit.id}/')
		self.assertTemplateUsed(response, 'bmicalcu.html')
		
	def test_pass_v_info_to_template(self):
		Mil1 = unit.objects.create()
		Mil2 = unit.objects.create()
		passBMIList = unit.objects.create()
		response = self.client.get(f'/BMIList/{passBMIList.id}/')
		self.assertEqual(response.context['KId'],passBMIList)
		
class New_List_Test(TestCase):	
	def test_at_request(self):
		response = self.client.post('/BMIList/mgm2_url', data={'age':'Age'})
#		self.assertIn('age', response.content.decode())
#		self.assertTemplateUsed(response,'bmi.html')
		
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'Age')
		
	def test_palit_POST(self):
		response = self.client.post('/BMIList/mgm2_url', data={'age':'age'})
		newunit = unit.objects.first()
		self.assertRedirects(response, f'/BMIList/{newunit.id}/')
		
class  AddItemTest(TestCase):
	def test_nagadd_ngbagongpost(self):
		Mil1 = unit.objects.create()
		Mil2 = unit.objects.create()
		existingMil = unit.objects.create()
		self.client.post(f'/BMIList/{existingMil.id}/addItem', data={'age': 'New Age for existing'})
		self.assertEqual(Item.objects.count(),1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'New Age for existing')
		self.assertEqual(newItem.KeyId, existingMil)
		
	def test_redirects_to_list_view(self):
		Mil1 = unit.objects.create()
		Mil2 = unit.objects.create()
		Mil3 = unit.objects.create()
		existingMil = unit.objects.create()
		response = self.client.post(f'/BMIList/{existingMil.id}/addItem', data={'age': 'age'})
		self.assertRedirects(response, f'/BMIList/{existingMil.id}/')
		
		
		
#	def test_save_only_if_necessary(self):
#		response = self.client.get ('/')
#		self.assertEqual(Item.objects.count(), 0)
		
#	def test_at_request(self):
#		response = self.client.post('/', data={'age':'Age'})
#		self.assertIn('age', response.content.decode())
#		self.assertTemplateUsed(response,'bmi.html')
		
#		self.assertEqual(Item.objects.count(), 1)
#		newItem = Item.objects.first()
#		self.assertEqual(newItem.text, 'Age')
		
#	def test_palit_POST(self):
#		response = self.client.post('/', data={'age':'age'})
#		self.assertRedirects(response, 'BMIList/mgm_url')
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(response['location'], '/BMIList/mgm_url/')
		
'''	def test_template_display_items(self):
	        Item.objects.create(text= 'mgm1')
	        Item.objects.create(text= 'mgm2')
	        response = self.client.get('/')
	        self.assertIn('mgm1', response.content.decode())
	        self.assertIn('mgm2', response.content.decode())'''


		
	
		
#		self.assertEqual(response.status_code, 302)
#		self.assertRedirects(response, '/BMIList/mgm_url/')		
'''class CreateListTest(TestCase):

	def test_at_request(self):
		response = self.client.post('/', data={'age':'Age'})
#		self.assertIn('age', response.content.decode())
#		self.assertTemplateUsed(response,'bmi.html')
		
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'Age')
		
	def test_palit_POST(self):
		response = self.client.post('BMIList/newlist_url', data={'age':'age'})
		self.assertRedirects(response, 'BMIList/mgm_url')
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(response['location'], '/BMIList/mgm_url/')'''
	
