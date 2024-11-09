package com.magistuarmory.addon.item;

import com.magistuarmory.addon.EpicKnightsAddon;
import com.magistuarmory.addon.config.WeaponsConfig;
import com.magistuarmory.item.WeaponType;

public class AddonWeaponTypes
{
	public static final WeaponsConfig WEAPONS_CONFIG = EpicKnightsAddon.CONFIG.weapons;

	public static final WeaponType BAR_MACE = new WeaponType(WEAPONS_CONFIG.barMace.baseAttackDamage, WEAPONS_CONFIG.barMace.baseAttackSpeed, WEAPONS_CONFIG.barMace.bonusAttackReach, 0.05f, 2.6f, 0, WEAPONS_CONFIG.barMace.enabled);
	public static final WeaponType BATTLEAXE = new WeaponType(WEAPONS_CONFIG.battleaxe.baseAttackDamage, WEAPONS_CONFIG.battleaxe.baseAttackSpeed, WEAPONS_CONFIG.battleaxe.bonusAttackReach, 0.02f, 2.3f, 0, WEAPONS_CONFIG.battleaxe.enabled);
	public static final WeaponType CROW_BEAK = new WeaponType(WEAPONS_CONFIG.crowBeak.baseAttackDamage, WEAPONS_CONFIG.crowBeak.baseAttackSpeed, WEAPONS_CONFIG.crowBeak.bonusAttackReach, 0.03f, 2.0f, 15, WEAPONS_CONFIG.crowBeak.enabled).setTwoHanded(9);
	public static final WeaponType FRANCISCA_AXE = new WeaponType(WEAPONS_CONFIG.franciscaAxe.baseAttackDamage, WEAPONS_CONFIG.franciscaAxe.baseAttackSpeed, WEAPONS_CONFIG.franciscaAxe.bonusAttackReach, 0.00f, 2.4f, 0, WEAPONS_CONFIG.franciscaAxe.enabled);
	public static final WeaponType ROUND_MACE = new WeaponType(WEAPONS_CONFIG.roundMace.baseAttackDamage, WEAPONS_CONFIG.roundMace.baseAttackSpeed, WEAPONS_CONFIG.roundMace.bonusAttackReach, 0.05f, 2.0f, 0, WEAPONS_CONFIG.roundMace.enabled);
	public static final WeaponType WAR_AXE = new WeaponType(WEAPONS_CONFIG.warAxe.baseAttackDamage, WEAPONS_CONFIG.warAxe.baseAttackSpeed, WEAPONS_CONFIG.warAxe.bonusAttackReach, 0.02f, 2.3f, 0, WEAPONS_CONFIG.warAxe.enabled);
	public static final WeaponType WAR_HAMMER = new WeaponType(WEAPONS_CONFIG.warHammer.baseAttackDamage, WEAPONS_CONFIG.warHammer.baseAttackSpeed, WEAPONS_CONFIG.warHammer.bonusAttackReach, 0.03f, 2.0f, 5, WEAPONS_CONFIG.warHammer.enabled);
	public static final WeaponType BOLLOCK_DAGGER = new WeaponType(WEAPONS_CONFIG.bollockDagger.baseAttackDamage, WEAPONS_CONFIG.bollockDagger.baseAttackSpeed, WEAPONS_CONFIG.bollockDagger.bonusAttackReach, 0.00f, 0.6f, 0, WEAPONS_CONFIG.bollockDagger.enabled);
	public static final WeaponType DAGGER = new WeaponType(WEAPONS_CONFIG.dagger.baseAttackDamage, WEAPONS_CONFIG.dagger.baseAttackSpeed, WEAPONS_CONFIG.dagger.bonusAttackReach, 0.00f, 0.6f, 0, WEAPONS_CONFIG.dagger.enabled);
	public static final WeaponType PARRYING_DAGGER = new WeaponType(WEAPONS_CONFIG.parryingDagger.baseAttackDamage, WEAPONS_CONFIG.parryingDagger.baseAttackSpeed, WEAPONS_CONFIG.parryingDagger.bonusAttackReach, 0.00f, 0.6f, 0, WEAPONS_CONFIG.parryingDagger.enabled);
	public static final WeaponType RONDEL_DAGGER = new WeaponType(WEAPONS_CONFIG.rondelDagger.baseAttackDamage, WEAPONS_CONFIG.rondelDagger.baseAttackSpeed, WEAPONS_CONFIG.rondelDagger.bonusAttackReach, 0.00f, 0.6f, 8, WEAPONS_CONFIG.rondelDagger.enabled);
	public static final WeaponType SICKLE = new WeaponType(WEAPONS_CONFIG.sickle.baseAttackDamage, WEAPONS_CONFIG.sickle.baseAttackSpeed, WEAPONS_CONFIG.sickle.bonusAttackReach, 0.00f, 0.6f, 0, WEAPONS_CONFIG.sickle.enabled);
	public static final WeaponType EXECUTIONERS_SWORD = new WeaponType(WEAPONS_CONFIG.executionersSword.baseAttackDamage, WEAPONS_CONFIG.executionersSword.baseAttackSpeed, WEAPONS_CONFIG.executionersSword.bonusAttackReach, 0.05f, 3.9f, 0, WEAPONS_CONFIG.executionersSword.enabled).setTwoHanded(2).setMaxBlockDamage(4.00f);
	public static final WeaponType GERMAN_GREATSWORD = new WeaponType(WEAPONS_CONFIG.germanGreatsword.baseAttackDamage, WEAPONS_CONFIG.germanGreatsword.baseAttackSpeed, WEAPONS_CONFIG.germanGreatsword.bonusAttackReach, 0.05f, 3.9f, 0, WEAPONS_CONFIG.germanGreatsword.enabled).setTwoHanded(2).setMaxBlockDamage(3.00f);
	public static final WeaponType TWO_HANDED_MESSER = new WeaponType(WEAPONS_CONFIG.twoHandedMesser.baseAttackDamage, WEAPONS_CONFIG.twoHandedMesser.baseAttackSpeed, WEAPONS_CONFIG.twoHandedMesser.bonusAttackReach, 0.05f, 3.8f, 0, WEAPONS_CONFIG.twoHandedMesser.enabled).setMaxBlockDamage(3.00f);
	public static final WeaponType ENGLISH_POLEAXE = new WeaponType(WEAPONS_CONFIG.englishPoleaxe.baseAttackDamage, WEAPONS_CONFIG.englishPoleaxe.baseAttackSpeed, WEAPONS_CONFIG.englishPoleaxe.bonusAttackReach, 0.05f, 4.0f, 1, WEAPONS_CONFIG.englishPoleaxe.enabled).setTwoHanded(2).setMaxBlockDamage(4.00f).setHalberd();
	public static final WeaponType FRENCH_HALBERD = new WeaponType(WEAPONS_CONFIG.frenchHalberd.baseAttackDamage, WEAPONS_CONFIG.frenchHalberd.baseAttackSpeed, WEAPONS_CONFIG.frenchHalberd.bonusAttackReach, 0.05f, 4.1f, 3, WEAPONS_CONFIG.frenchHalberd.enabled).setTwoHanded(2).setMaxBlockDamage(2.00f).setHalberd();
	public static final WeaponType ITALIAN_POLEAXE = new WeaponType(WEAPONS_CONFIG.italianPoleaxe.baseAttackDamage, WEAPONS_CONFIG.italianPoleaxe.baseAttackSpeed, WEAPONS_CONFIG.italianPoleaxe.bonusAttackReach, 0.04f, 3.8f, 0, WEAPONS_CONFIG.italianPoleaxe.enabled).setTwoHanded(2).setMaxBlockDamage(4.00f).setHalberd();
	public static final WeaponType SWISS_HALBERD = new WeaponType(WEAPONS_CONFIG.swissHalberd.baseAttackDamage, WEAPONS_CONFIG.swissHalberd.baseAttackSpeed, WEAPONS_CONFIG.swissHalberd.bonusAttackReach, 0.04f, 3.8f, 0, WEAPONS_CONFIG.swissHalberd.enabled).setTwoHanded(2).setMaxBlockDamage(2.00f).setHalberd();
	public static final WeaponType LANCE = new WeaponType(WEAPONS_CONFIG.lance.baseAttackDamage, WEAPONS_CONFIG.lance.baseAttackSpeed, WEAPONS_CONFIG.lance.bonusAttackReach, 0.00f, 3.0f, 0, WEAPONS_CONFIG.lance.enabled);
	public static final WeaponType BROADAXE = new WeaponType(WEAPONS_CONFIG.broadaxe.baseAttackDamage, WEAPONS_CONFIG.broadaxe.baseAttackSpeed, WEAPONS_CONFIG.broadaxe.bonusAttackReach, 0.05f, 3.5f, 0, WEAPONS_CONFIG.broadaxe.enabled).setTwoHanded(2).setMaxBlockDamage(3.00f);
	public static final WeaponType DANEAXE = new WeaponType(WEAPONS_CONFIG.daneaxe.baseAttackDamage, WEAPONS_CONFIG.daneaxe.baseAttackSpeed, WEAPONS_CONFIG.daneaxe.bonusAttackReach, 0.05f, 2.5f, 0, WEAPONS_CONFIG.daneaxe.enabled).setTwoHanded(2).setMaxBlockDamage(4.00f);
	public static final WeaponType GALLOWGLASS_AXE = new WeaponType(WEAPONS_CONFIG.gallowglassAxe.baseAttackDamage, WEAPONS_CONFIG.gallowglassAxe.baseAttackSpeed, WEAPONS_CONFIG.gallowglassAxe.bonusAttackReach, 0.05f, 2.5f, 0, WEAPONS_CONFIG.gallowglassAxe.enabled).setTwoHanded(2).setMaxBlockDamage(4.00f);
	public static final WeaponType HAMMER_SPEAR = new WeaponType(WEAPONS_CONFIG.hammerSpear.baseAttackDamage, WEAPONS_CONFIG.hammerSpear.baseAttackSpeed, WEAPONS_CONFIG.hammerSpear.bonusAttackReach, 0.05f, 3.5f, 0, WEAPONS_CONFIG.hammerSpear.enabled).setTwoHanded(2).setMaxBlockDamage(3.00f);
	public static final WeaponType TWO_HANDED_EVENING_STAR = new WeaponType(WEAPONS_CONFIG.twoHandedEveningStar.baseAttackDamage, WEAPONS_CONFIG.twoHandedEveningStar.baseAttackSpeed, WEAPONS_CONFIG.twoHandedEveningStar.bonusAttackReach, 0.05f, 3.5f, 0, WEAPONS_CONFIG.twoHandedEveningStar.enabled).setTwoHanded(2).setMaxBlockDamage(3.00f);
	public static final WeaponType CAVALRY_SABRE = new WeaponType(WEAPONS_CONFIG.cavalrySabre.baseAttackDamage, WEAPONS_CONFIG.cavalrySabre.baseAttackSpeed, WEAPONS_CONFIG.cavalrySabre.bonusAttackReach, 0.00f, 1.6f, 0, WEAPONS_CONFIG.cavalrySabre.enabled).setMaxBlockDamage(4.00f);
	public static final WeaponType CUTLASS = new WeaponType(WEAPONS_CONFIG.cutlass.baseAttackDamage, WEAPONS_CONFIG.cutlass.baseAttackSpeed, WEAPONS_CONFIG.cutlass.bonusAttackReach, 0.04f, 1.2f, 0, WEAPONS_CONFIG.cutlass.enabled).setTwoHanded(1).setMaxBlockDamage(4.00f);
	public static final WeaponType FALCHION = new WeaponType(WEAPONS_CONFIG.falchion.baseAttackDamage, WEAPONS_CONFIG.falchion.baseAttackSpeed, WEAPONS_CONFIG.falchion.bonusAttackReach, 0.00f, 1.6f, 0, WEAPONS_CONFIG.falchion.enabled).setMaxBlockDamage(4.00f);
	public static final WeaponType FEDER = new WeaponType(WEAPONS_CONFIG.feder.baseAttackDamage, WEAPONS_CONFIG.feder.baseAttackSpeed, WEAPONS_CONFIG.feder.bonusAttackReach, 0.02f, 1.6f, 2, WEAPONS_CONFIG.feder.enabled).setTwoHanded(1).setMaxBlockDamage(4.00f);
	public static final WeaponType GRAND_FALCHION = new WeaponType(WEAPONS_CONFIG.grandFalchion.baseAttackDamage, WEAPONS_CONFIG.grandFalchion.baseAttackSpeed, WEAPONS_CONFIG.grandFalchion.bonusAttackReach, 0.06f, 2.3f, 0, WEAPONS_CONFIG.grandFalchion.enabled).setTwoHanded(2).setMaxBlockDamage(4.00f);
	public static final WeaponType KING_SWORD = new WeaponType(WEAPONS_CONFIG.kingSword.baseAttackDamage, WEAPONS_CONFIG.kingSword.baseAttackSpeed, WEAPONS_CONFIG.kingSword.bonusAttackReach, 0.02f, 1.8f, 0, WEAPONS_CONFIG.kingSword.enabled).setTwoHanded(1).setMaxBlockDamage(5.00f);
	public static final WeaponType LONGSWORD = new WeaponType(WEAPONS_CONFIG.longsword.baseAttackDamage, WEAPONS_CONFIG.longsword.baseAttackSpeed, WEAPONS_CONFIG.longsword.bonusAttackReach, 0.02f, 2.5f, 0, WEAPONS_CONFIG.longsword.enabled).setTwoHanded(1).setMaxBlockDamage(5.00f);
	public static final WeaponType LONG_SEAX = new WeaponType(WEAPONS_CONFIG.longSeax.baseAttackDamage, WEAPONS_CONFIG.longSeax.baseAttackSpeed, WEAPONS_CONFIG.longSeax.bonusAttackReach, 0.02f, 2.1f, 0, WEAPONS_CONFIG.longSeax.enabled).setMaxBlockDamage(3.00f);
	public static final WeaponType MACIEJOWSKI_MESSER = new WeaponType(WEAPONS_CONFIG.maciejowskiMesser.baseAttackDamage, WEAPONS_CONFIG.maciejowskiMesser.baseAttackSpeed, WEAPONS_CONFIG.maciejowskiMesser.bonusAttackReach, 0.00f, 1.6f, 0, WEAPONS_CONFIG.maciejowskiMesser.enabled).setMaxBlockDamage(4.00f);
	public static final WeaponType MESSER_SWORD = new WeaponType(WEAPONS_CONFIG.messerSword.baseAttackDamage, WEAPONS_CONFIG.messerSword.baseAttackSpeed, WEAPONS_CONFIG.messerSword.bonusAttackReach, 0.02f, 1.2f, 0, WEAPONS_CONFIG.messerSword.enabled).setMaxBlockDamage(5.00f);
	public static final WeaponType RAPIER = new WeaponType(WEAPONS_CONFIG.rapier.baseAttackDamage, WEAPONS_CONFIG.rapier.baseAttackSpeed, WEAPONS_CONFIG.rapier.bonusAttackReach, 0.00f, 1.2f, 5, WEAPONS_CONFIG.rapier.enabled).setMaxBlockDamage(6.00f);
	public static final WeaponType SCIMITAR = new WeaponType(WEAPONS_CONFIG.scimitar.baseAttackDamage, WEAPONS_CONFIG.scimitar.baseAttackSpeed, WEAPONS_CONFIG.scimitar.bonusAttackReach, 0.04f, 2.1f, 0, WEAPONS_CONFIG.scimitar.enabled).setTwoHanded(1).setMaxBlockDamage(4.00f);
	public static final WeaponType SIDESWORD = new WeaponType(WEAPONS_CONFIG.sidesword.baseAttackDamage, WEAPONS_CONFIG.sidesword.baseAttackSpeed, WEAPONS_CONFIG.sidesword.bonusAttackReach, 0.00f, 1.5f, 2, WEAPONS_CONFIG.sidesword.enabled).setMaxBlockDamage(6.00f);
	public static final WeaponType TRAINING_SWORD = new WeaponType(WEAPONS_CONFIG.trainingSword.baseAttackDamage, WEAPONS_CONFIG.trainingSword.baseAttackSpeed, WEAPONS_CONFIG.trainingSword.bonusAttackReach, 0.02f, 1.6f, 0, WEAPONS_CONFIG.trainingSword.enabled).setTwoHanded(1).setMaxBlockDamage(4.00f);
	public static final WeaponType BILLHOOK = new WeaponType(WEAPONS_CONFIG.billhook.baseAttackDamage, WEAPONS_CONFIG.billhook.baseAttackSpeed, WEAPONS_CONFIG.billhook.bonusAttackReach, 0.00f, 3.0f, 0, WEAPONS_CONFIG.billhook.enabled).setTwoHanded(1).setMaxBlockDamage(2.00f).setHalberd();
	public static final WeaponType BOAR_SPEAR = new WeaponType(WEAPONS_CONFIG.boarSpear.baseAttackDamage, WEAPONS_CONFIG.boarSpear.baseAttackSpeed, WEAPONS_CONFIG.boarSpear.bonusAttackReach, 0.00f, 1.8f, 0, WEAPONS_CONFIG.boarSpear.enabled).setTwoHanded(1).setMaxBlockDamage(2.00f);
	public static final WeaponType FAUCHARD = new WeaponType(WEAPONS_CONFIG.fauchard.baseAttackDamage, WEAPONS_CONFIG.fauchard.baseAttackSpeed, WEAPONS_CONFIG.fauchard.bonusAttackReach, 0.01f, 3.0f, 0, WEAPONS_CONFIG.fauchard.enabled).setTwoHanded(1).setMaxBlockDamage(1.00f);
	public static final WeaponType GLAIVE = new WeaponType(WEAPONS_CONFIG.glaive.baseAttackDamage, WEAPONS_CONFIG.glaive.baseAttackSpeed, WEAPONS_CONFIG.glaive.bonusAttackReach, 0.00f, 2.5f, 0, WEAPONS_CONFIG.glaive.enabled).setTwoHanded(1).setMaxBlockDamage(3.00f);
	public static final WeaponType GOEDENDAG = new WeaponType(WEAPONS_CONFIG.goedendag.baseAttackDamage, WEAPONS_CONFIG.goedendag.baseAttackSpeed, WEAPONS_CONFIG.goedendag.bonusAttackReach, 0.00f, 2.5f, 16, WEAPONS_CONFIG.goedendag.enabled).setTwoHanded(2);
	public static final WeaponType MILITARY_FORK = new WeaponType(WEAPONS_CONFIG.militaryFork.baseAttackDamage, WEAPONS_CONFIG.militaryFork.baseAttackSpeed, WEAPONS_CONFIG.militaryFork.bonusAttackReach, 0.05f, 2.2f, 0, WEAPONS_CONFIG.militaryFork.enabled);
	public static final WeaponType PARTISAN = new WeaponType(WEAPONS_CONFIG.partisan.baseAttackDamage, WEAPONS_CONFIG.partisan.baseAttackSpeed, WEAPONS_CONFIG.partisan.bonusAttackReach, 0.00f, 2.5f, 0, WEAPONS_CONFIG.partisan.enabled).setTwoHanded(1).setMaxBlockDamage(5.00f);
	public static final WeaponType SCYTHE = new WeaponType(WEAPONS_CONFIG.scythe.baseAttackDamage, WEAPONS_CONFIG.scythe.baseAttackSpeed, WEAPONS_CONFIG.scythe.bonusAttackReach, 0.04f, 3.0f, 0, WEAPONS_CONFIG.scythe.enabled).setTwoHanded(2);
	public static final WeaponType SHORT_SPEAR = new WeaponType(WEAPONS_CONFIG.shortSpear.baseAttackDamage, WEAPONS_CONFIG.shortSpear.baseAttackSpeed, WEAPONS_CONFIG.shortSpear.bonusAttackReach, 0.00f, 1.7f, 0, WEAPONS_CONFIG.shortSpear.enabled).setTwoHanded(1).setMaxBlockDamage(2.00f);
	public static final WeaponType VOULGE = new WeaponType(WEAPONS_CONFIG.voulge.baseAttackDamage, WEAPONS_CONFIG.voulge.baseAttackSpeed, WEAPONS_CONFIG.voulge.bonusAttackReach, 0.00f, 2.5f, 0, WEAPONS_CONFIG.voulge.enabled).setTwoHanded(1).setMaxBlockDamage(1.00f).setHalberd();
	public static final WeaponType WELSH_GUISARME = new WeaponType(WEAPONS_CONFIG.welshGuisarme.baseAttackDamage, WEAPONS_CONFIG.welshGuisarme.baseAttackSpeed, WEAPONS_CONFIG.welshGuisarme.bonusAttackReach, 0.00f, 2.5f, 0, WEAPONS_CONFIG.welshGuisarme.enabled).setTwoHanded(1).setMaxBlockDamage(3.00f);
	public static final WeaponType ARMING_SWORD_TYPE_XIII = new WeaponType(WEAPONS_CONFIG.armingSwordTypeXiii.baseAttackDamage, WEAPONS_CONFIG.armingSwordTypeXiii.baseAttackSpeed, WEAPONS_CONFIG.armingSwordTypeXiii.bonusAttackReach, 0.00f, 1.1f, 0, WEAPONS_CONFIG.armingSwordTypeXiii.enabled);
	public static final WeaponType ARMING_SWORD_TYPE_XIV = new WeaponType(WEAPONS_CONFIG.armingSwordTypeXiv.baseAttackDamage, WEAPONS_CONFIG.armingSwordTypeXiv.baseAttackSpeed, WEAPONS_CONFIG.armingSwordTypeXiv.bonusAttackReach, 0.00f, 1.1f, 0, WEAPONS_CONFIG.armingSwordTypeXiv.enabled);
	public static final WeaponType ARMING_SWORD_TYPE_XV = new WeaponType(WEAPONS_CONFIG.armingSwordTypeXv.baseAttackDamage, WEAPONS_CONFIG.armingSwordTypeXv.baseAttackSpeed, WEAPONS_CONFIG.armingSwordTypeXv.bonusAttackReach, 0.00f, 1.1f, 0, WEAPONS_CONFIG.armingSwordTypeXv.enabled);
	public static final WeaponType RICH_SAXON_SWORD = new WeaponType(WEAPONS_CONFIG.richSaxonSword.baseAttackDamage, WEAPONS_CONFIG.richSaxonSword.baseAttackSpeed, WEAPONS_CONFIG.richSaxonSword.bonusAttackReach, 0.00f, 1.1f, 0, WEAPONS_CONFIG.richSaxonSword.enabled);
	public static final WeaponType SABRE = new WeaponType(WEAPONS_CONFIG.sabre.baseAttackDamage, WEAPONS_CONFIG.sabre.baseAttackSpeed, WEAPONS_CONFIG.sabre.bonusAttackReach, 0.00f, 1.5f, 0, WEAPONS_CONFIG.sabre.enabled).setMaxBlockDamage(4.00f);
	public static final WeaponType SAXON_SWORD = new WeaponType(WEAPONS_CONFIG.saxonSword.baseAttackDamage, WEAPONS_CONFIG.saxonSword.baseAttackSpeed, WEAPONS_CONFIG.saxonSword.bonusAttackReach, 0.00f, 1.1f, 0, WEAPONS_CONFIG.saxonSword.enabled);
	public static final WeaponType SHORT_SEAX = new WeaponType(WEAPONS_CONFIG.shortSeax.baseAttackDamage, WEAPONS_CONFIG.shortSeax.baseAttackSpeed, WEAPONS_CONFIG.shortSeax.bonusAttackReach, 0.00f, 0.9f, 0, WEAPONS_CONFIG.shortSeax.enabled);
	public static final WeaponType SWORDBREAKER = new WeaponType(WEAPONS_CONFIG.swordbreaker.baseAttackDamage, WEAPONS_CONFIG.swordbreaker.baseAttackSpeed, WEAPONS_CONFIG.swordbreaker.bonusAttackReach, 0.00f, 1.3f, 0, WEAPONS_CONFIG.swordbreaker.enabled).setMaxBlockDamage(10.00f);
}